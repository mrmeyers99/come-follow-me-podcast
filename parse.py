import requests
import re
from lxml import etree
from io import StringIO
from datetime import datetime

r = requests.get(url = "https://www.lds.org/study/manual/come-follow-me-for-individuals-and-families-new-testament-2019/02?lang=eng")

parser = etree.HTMLParser(encoding="utf-8")
r.encoding = "utf-8"
print(r.encoding)
#print(r.text)
tree = etree.parse(StringIO(r.text), parser)
res = tree.xpath("/html/head/meta[@name='description']/@content")[0]
print(res)
m = re.search('(\w+)\s*(\d+)–([A-Za-z]*)\s*(\d+)\.\s+(.*):\s*‘(.*)’', res)
#re.search('(\w+\s*\d+–\d+)\.\s+(.*):\s*‘(.*)’', res)
#re.search('(.*)\.\s*(.*):\s*(.*)', res)
start_month = m.group(1)
start_date = m.group(2)
end_month = m.group(3)
end_date = m.group(4)
chapters = m.group(5).split('; ')
title = m.group(6)
print(start_month, 'start_date =', start_date, 'end_month =', end_month, 'end_date =', end_date, chapters, title)

start_date = datetime.strptime(start_month + ' ' + start_date + ' 2019', '%B %d %Y')
end_date = datetime.strptime((end_month or start_month) + ' ' + end_date + ' 2019', '%B %d %Y')
print(start_date, '-', end_date)

print("""<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:itunesu="http://www.itunesu.com/feed" version="2.0">
<channel>
<link>http://www.YourSite.com</link>
<language>en-us</language>
<copyright>&#xA9;2013</copyright>
<webMaster>your@email.com (Your Name)</webMaster>
<managingEditor>your@email.com (Your Name)</managingEditor>
<image>
<url>http://www.YourSite.com/ImageSize300X300.jpg</url>
<title>Title or description of your logo</title>
<link>http://www.YourSite.com</link>
</image>
<itunes:owner>
<itunes:name>Michael Meyers</itunes:name>
<itunes:email>mrmeyers99@gmail.com</itunes:email>
</itunes:owner>
<itunes:category text="Education">
<itunes:category text="Higher Education" />
</itunes:category>
<itunes:keywords>separate, by, comma, and, space</itunes:keywords>
<itunes:explicit>no</itunes:explicit>
<itunes:image href="http://www.YourSite.com/ImageSize300X300.jpg" />
<atom:link href="http://www.YourSite.com/feed.xml" rel="self" type="application/rss+xml" />
<pubDate>Sun, 01 Jan 2012 00:00:00 EST</pubDate>
<title>Verbose title of the podcast</title>
<itunes:author>College, school, or department owning the podcast</itunes:author>
<description>Verbose description of the podcast.</description>
<itunes:summary>Duplicate of above verbose description.</itunes:summary>
<itunes:subtitle>Short description of the podcast - 255 character max.</itunes:subtitle>
<lastBuildDate>Thu, 02 Feb 2012 00:00:00 EST</lastBuildDate>""")


for chapter in chapters:
    split = chapter.split(' ')
    url = 'https://media2.ldscdn.org/assets/scriptures/the-new-testament/2015-11-0010-' + split[0].lower() + '-' + ('%02d' % int(split[1])) + '-male-voice-64k-eng.mp3?download=true'
    print("""
<item>
  <title>""" + title + ' - ' + chapter + """</title>
  <description>Verbose description of the episode.</description>
  <itunes:summary></itunes:summary>
  <itunes:subtitle></itunes:subtitle>
  <itunesu:category itunesu:code="112" />
  <enclosure url=\"""" + url + """\" type="audio/mpeg" length="1" />
  <guid>""" + url + """</guid>
  <itunes:duration>00:00:00</itunes:duration>
  <pubDate>""" + start_date.strftime('%a, %d %b %Y %H:%M:%S EST') + """</pubDate>
</item>""")

print("""
</channel>
</rss>""")