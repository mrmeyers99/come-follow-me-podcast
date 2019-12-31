import math

from app import app
from datetime import datetime, timedelta
import json

from app.client import Client
from flask import Response
from flask_restful import reqparse
from xml.sax.saxutils import escape

@app.route('/')
@app.route('/index')
def index():

    parser = reqparse.RequestParser()
    parser.add_argument('speadOverDays', type=int, store_missing=True, default=5)
    args = parser.parse_args()

    client = Client()
    lesson = client.get_lesson_for_date(datetime.today())

    info = """<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:itunesu="http://www.itunesu.com/feed" version="2.0">
<channel>
<link>https://www.lds.org</link>
<language>en-us</language>
<copyright>&#xA9;2019</copyright>
<webMaster>mrmeyers99@gmail.com (Michael)</webMaster>
<managingEditor>mrmeyers99@gmail.com (Michael)</managingEditor>
<image>
<url>http://www.YourSite.com/ImageSize300X300.jpg</url>
<title>Title or description of your logo</title>
<link>http://www.YourSite.com</link>
</image>
<itunes:owner>
<itunes:name>Michael Meyers</itunes:name>
<itunes:email>mrmeyers99@gmail.com</itunes:email>
</itunes:owner>
<itunes:category text="Religion">
<itunes:category text="Spirituality" />
</itunes:category>
<itunes:keywords>come, follow, me</itunes:keywords>
<itunes:explicit>no</itunes:explicit>
<itunes:image href="https://content.ldschurch.org/templesldsorg/bc/Temples/photo-galleries/salt-lake-city-utah/2018/400x640/slctemple2.jpg" />
<atom:link href="http://www.YourSite.com/feed.xml" rel="self" type="application/rss+xml" />
<title>Come Follow Me Scriptures</title>
<itunes:author></itunes:author>
<description></description>
<itunes:summary></itunes:summary>
<itunes:subtitle></itunes:subtitle>"""

    chapter_date = lesson['start_date']
    chapters = lesson['chapters']

    for index in range(0, len(chapters)):
        if chapter_date > datetime.now():
            break

        info += """
<item>
  <title>""" + lesson['title'] + ' - ' + chapters[index]['name'] + """</title>
  <description>""" + lesson['title'] + ' - ' + chapters[index]['name'] + """</description>
  <itunes:summary></itunes:summary>
  <itunes:subtitle></itunes:subtitle>
  <itunesu:category itunesu:code="112" />
  <enclosure url=\"""" + escape(chapters[index]['url']) + """\" type="audio/mpeg" />
  <guid>""" + escape(chapters[index]['url']) + """</guid>
  <pubDate>""" + chapter_date.strftime('%a, %d %b %Y %H:%M:%S EST') + """</pubDate>
</item>"""
        if index % math.ceil(len(chapters) / args['speadOverDays']) == 0:
            chapter_date = chapter_date + timedelta(days=1)
        index += 1

    info += """
</channel>
</rss>"""

    return Response(info, mimetype='text/xml')


@app.route('/urls')
def urls():
    d2 = json.load(open("book_urls.json"))
    return json.dumps(d2)
