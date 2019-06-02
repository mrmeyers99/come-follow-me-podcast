from app import app
from datetime import datetime
import json

from app.client import Client
from flask import Response

@app.route('/')
@app.route('/index')
def index():
    current_week = int(datetime.today().strftime("%V")) - 1

    client = Client()
    lesson = client.get_lesson_for_week(current_week)

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

    for chapter in lesson['chapters']:

        info += """
<item>
  <title>""" + lesson['title'] + ' - ' + chapter['name'] + """</title>
  <description>""" + lesson['title'] + ' - ' + chapter['name'] + """</description>
  <itunes:summary></itunes:summary>
  <itunes:subtitle></itunes:subtitle>
  <itunesu:category itunesu:code="112" />
  <enclosure url=\"""" + chapter['url'] + """\" type="audio/mpeg" />
  <guid>""" + chapter['url'] + """</guid>
  <pubDate>""" + lesson['start_date'].strftime('%a, %d %b %Y %H:%M:%S EST') + """</pubDate>
</item>"""
    info += """
</channel>
</rss>"""
    return Response(info, mimetype='text/xml')


@app.route('/urls')
def urls():
    d2 = json.load(open("book_urls.json"))
    return json.dumps(d2)
