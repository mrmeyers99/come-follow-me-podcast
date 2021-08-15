# -*- coding: utf-8 -

import requests
import re
from lxml import etree
from io import StringIO
from datetime import datetime
import json


class Client:

    @staticmethod
    def find_lesson(calendar, date):
        for lesson in calendar:
            print(lesson)
            if datetime.strptime(lesson['begin'], '%B %d %Y') <= date <= datetime.strptime(lesson['end'], '%B %d %Y'):
                return lesson
        raise Exception("Could not find lesson for " + date.strftime("%d/%m/%Y"))

    def get_lesson_for_date(self, date):
        calendar = json.load(open("calendar.json"))
        urls = json.load(open("book_urls.json"))

        lesson = self.find_lesson(calendar, date)

        return {
            "title": lesson['title'],
            "start_date": datetime.strptime(lesson['begin'], '%B %d %Y'),
            "end_date": datetime.strptime(lesson['end'], '%B %d %Y'),
            "chapters": [{"name": c.replace(u'\xa0', u' '), "url": u}
                         for c in lesson['chapters'] for u in urls[c]]
        }
        # print(start_month, 'start_date =', start_date, 'end_month =', end_month, 'end_date =', end_date, chapters, title)
        # print(json.dumps(chapters_json))
        # print(json.dumps(week_json))

