# coding=utf8

import requests
import re
from lxml import etree
from io import StringIO
from datetime import datetime
import json


class Client:

#https://media2.ldscdn.org/assets/scriptures/the-pearl-of-great-price/2015-11-0140-joseph-smith-matthew-male-voice-64k-eng.mp3?download=true
    def get_episodes_for_week(self, week):

        r = requests.get(url="https://www.lds.org/study/manual/come-follow-me-for-individuals-and-families-new-testament-2019/" + str(week) + "?lang=eng")

        parser = etree.HTMLParser(encoding="utf-8")
        r.encoding = "utf-8"
        print(r.encoding)
        #print(r.text)
        tree = etree.parse(StringIO(r.text), parser)
        res = tree.xpath("/html/head/meta[@name='description']/@content")[0]
        print(res)
        regex = r"(\w+)\s*(\d+)–([A-Za-z]*)\s*(\d+)\.\s+(.*):\s*‘(.*)’"
        matches = re.finditer(regex, res, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):

            print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1

                print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


        m = re.search("(\\w+)\\s*(\\d+)–([A-Za-z]*)\\s*(\\d+)\\.\\s+(.*):\\s*‘(.*)’", res)
        #re.search('(\w+\s*\d+–\d+)\.\s+(.*):\s*‘(.*)’', res)
        #re.search('(.*)\.\s*(.*):\s*(.*)', res)
        start_month = m.group(1)
        start_date = m.group(2)
        end_month = m.group(3)
        end_date = m.group(4)
        chapters = m.group(5).split('; ')
        title = m.group(6)

        chapters_json = map(lambda c: {
            "name": c,
            "url": "x"
        }, chapters)
        week_json = {
            "start_date": datetime.strptime(start_month + ' ' + start_date + ' 2019', '%B %d %Y'),
            "end_date": datetime.strptime((end_month or start_month) + ' ' + end_date + ' 2019', '%B %d %Y'),
            "chapters": {
                chapters_json
            }
        }
        print(start_month, 'start_date =', start_date, 'end_month =', end_month, 'end_date =', end_date, chapters, title)
        print(json.dumps(chapters_json))

