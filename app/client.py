# -*- coding: utf-8 -

import requests
import re
from lxml import etree
from io import StringIO
from datetime import datetime
import json


class Client:

    def split_chapters(self, chapter_info):
        flattened_chapters = []
        chapters = chapter_info.split('; ')
        for chapter in chapters:
            if chapter == 'Enos–Words of Mormon':
                flattened_chapters.append('Enos 1')
                flattened_chapters.append('Jarom 1')
                flattened_chapters.append('Omni 1')
                flattened_chapters.append('Words of Mormon 1')
            else:
                m = re.search("([\\w\\s]+)\\s+(\\d+)–(\\d+)", chapter)

                if m:
                    flattened_chapters.extend(list(map(lambda x: m.group(1) + ' ' + str(x), range(int(m.group(2)), int(m.group(3)) + 1))))
                else:
                    flattened_chapters.append(chapter)
        print(flattened_chapters)
        return flattened_chapters

    def find_lesson(self, calendar, date):
        for lesson in calendar:
            print(lesson)
            if datetime.strptime(lesson['begin'], '%B %d %Y') <= date <= datetime.strptime(lesson['end'], '%B %d %Y'):
                return lesson
        raise Exception('Could not find lesson')

    def get_lesson_for_date(self, date):
        calendar = json.load(open("calendar.json"))
        urls = json.load(open("book_urls.json"))

        lesson = self.find_lesson(calendar, date)
        chapters = self.split_chapters(lesson['chapters'])

        return {
            "title": lesson['title'],
            "start_date": lesson['begin'],
            "end_date": lesson['end'],
            "chapters": [{"name": c.replace(u'\xa0', u' '), "url": u}
                         for c in chapters for u in urls[c.replace(u'\xa0', u' ')]]
        }
        # print(start_month, 'start_date =', start_date, 'end_month =', end_month, 'end_date =', end_date, chapters, title)
        # print(json.dumps(chapters_json))
        # print(json.dumps(week_json))

