import requests
from lxml import etree
from io import StringIO
from datetime import datetime
import json

import re

#from the old client

def split_chapters(chapter_info):
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
                flattened_chapters.extend(list(map(lambda x: m.group(1).replace(u'\xa0', u' ') + ' ' + str(x), range(int(m.group(2)), int(m.group(3)) + 1))))
            else:
                flattened_chapters.append(chapter.replace(u'\xa0', u' '))
    print(flattened_chapters)
    return flattened_chapters

year = 2020
if year == 2019:
    manual = "come-follow-me-for-individuals-and-families-new-testament-2019"
else:
    manual = "come-follow-me-for-individuals-and-families-book-of-mormon-2020"

lessons = []

def fetch_lesson_info(week, manual):
    r = requests.get(url="https://www.lds.org/study/manual/" + manual + "/" + f'{week:02}' + "?lang=eng")
    if r.status_code == 404:
        return None

    parser = etree.HTMLParser(encoding="utf-8")
    r.encoding = "utf-8"
    print(r.encoding)
    #print(r.text)
    tree = etree.parse(StringIO(r.text), parser)
    res = tree.xpath("/html/head/meta[@name='description']/@content")[0]
    print(res)
    # regex = r"(\w+)\s*(\d+)–([A-Za-z]*)\s*(\d+)\.\s*(.*)"
    # matches = re.finditer(regex, res, re.MULTILINE)
    #
    # for matchNum, match in enumerate(matches, start=1):
    #
    #     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #
    #     for groupNum in range(0, len(match.groups())):
    #         groupNum = groupNum + 1
    #
    #         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    m = re.search("(\\w+)\\s*(\\d+)–([A-Za-z]*)\\s*(\\d+)\\.\\s+(.*):\\s*[‘\"“]*([^[’\"”]*)[’\"”]*", res)

    if m is None:
        return None
    start_month = m.group(1)
    start_date = m.group(2)
    end_month = m.group(3)
    end_date = m.group(4)
    chapters = split_chapters(m.group(5))
    title = m.group(6)
    print(chapters)

    image_xpath = tree.xpath("//img[@id = 'figure1_img1']/@src")
    if len(image_xpath) > 0:
        print(image_xpath[0])
        image = image_xpath[0]
    else:
        image_xpath = tree.xpath("//img[@id = 'img1']/@src")
        print(image_xpath[0])
        image = image_xpath[0]

    lesson = {
        'chapters': chapters,
        'title': title,
        'begin': start_month + " " + start_date + " " + str(year),
        'end':  end_month if end_month != "" else start_month + " " + end_date + " " + str(year),
        'image': image
    }

    print(json.dumps(lesson))
    return lesson


def main():
    for week in range(1, 52):
        print(week)

        if week == 35 and year == 2020:
            lesson = {
                'chapters': ["Helaman 13", "Helaman 14", "Helaman 15", "Helaman 16"],
                'title': "Glad Tidings of Great Joy",
                'begin': "August 31 " + str(year),
                'end':  "September 6 " + str(year),
                'image': "https://assets.ldscdn.org/eb/b2/ebb2f52ceda4db2d4578989c9beda439b0a097be/samuel_the_lamanite_prophesies_friberg.png"
            }
        elif week == 41 and year == 2020:
            lesson = {
                'chapters': ["3 Nephi 27", "3 Nephi 28", "3 Nephi 29", "3 Nephi 30", "4 Nephi 1"],
                'title': "There Could Not Be a Happier People",
                'begin': "October 19 " + str(year),
                'end':  "October 25 " + str(year),
                'image': "https://assets.ldscdn.org/aa/1c/aa1c2e599c3271e598aa2f3701ff32d7848a6255/christ_prayer_art_lds.png"
            }
        elif week == 21 and year == 2020:
            lesson = {
                'chapters': ["Mosiah 29", "Alma 1", "Alma 2", "Alma 3", "Alma 4"],
                'title': "They Were Steadfast and Immovable",
                'begin': "May 25 " + str(year),
                'end':  "May 31 " + str(year),
                'image': "https://assets.ldscdn.org/e5/6e/e56e47a9820de4fbdbdd9eaa12808c02f5f518dd/alma_younger_talking_men_mormon.png"
            }
        elif week == 14 and year == 2020:
            lesson = {
                'chapters': ["Living Christ"],
                'title': "He Shall Rise with Healing in His Wings",
                'begin': "March 30 " + str(year),
                'end':  "April 12 " + str(year),
                'image': "https://assets.ldscdn.org/56/79/56797719a7244fdf4e6ce1d788712c2e95b72907/christ_risen_apostles.png"
            }
        else:
            lesson = fetch_lesson_info(week, manual)

        if lesson is not None:
            lessons.append(lesson)

    print(json.dumps(lessons, indent=2))


main()
