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

year = 2021
if year == 2019:
    manual = "come-follow-me-for-individuals-and-families-new-testament-2019"
elif year == 2020:
    manual = "come-follow-me-for-individuals-and-families-book-of-mormon-2020"
else:
    manual = "come-follow-me-for-individuals-and-families-doctrine-and-covenants-2021"

lessons = []

def fetch_lesson_info(week, manual):
    url = "https://www.lds.org/study/manual/" + manual + "/" + f'{week:02}' + "?lang=eng"
    print(url)
    r = requests.get(url=url)
    if r.status_code == 404:
        return None
    else:
        print(r.status_code)

    parser = etree.HTMLParser(encoding="utf-8")
    r.encoding = "utf-8"
    #print(r.encoding)
    #print(r.text)
    tree = etree.parse(StringIO(r.text), parser)
    res = tree.xpath("/html/head/meta[@name='title']/@content")[0]
    # print(res)
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
        'image': image,
        'url': url
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
        elif week == 2 and year == 2021:
            lesson = {
                'chapters': ["Joseph Smith - History"],
                'title': "I Saw a Pillar of Light",
                'begin': "January 4 " + str(year),
                'end':  "January 10 " + str(year),
                'image': "https://assets.ldscdn.org/db/82/db82cb1b5f5ca7536cb9602a7acb3c1e448c36a2/olsen_grove_sacred_lds_mormon.jpeg"
            }
        elif week == 3 and year == 2021:
            lesson = {
                'chapters': ["Doctrine and Covenants 2"],
                'title': "The Hearts of the Children Shall Turn to Their Fathers",
                'begin': "January 1 " + str(year),
                'end':  "January 17 " + str(year),
                'image': "https://assets.ldscdn.org/67/b5/67b5b9024bb68329b07a9b7eec3af9d78e8d2bcd/oil_painting_michael_malm.jpeg"
            }
        elif week == 7 and year == 2021:
            lesson =   {
               "chapters": [
                   "Doctrine and Covenants 12",
                   "Doctrine and Covenants 13"
               ],
               "title": "Upon You My Fellow Servants",
               "begin": "February 8 2021",
               "end": "February 14 2021",
               "image": "https://assets.ldscdn.org/13/fe/13fe00dc1d2cf16cd4510b7f909b0429d407bb5a/joseph_baptizes_oliver_cowdery_parson.jpeg"
           }
        elif week == 14 and year == 2021:
            lesson =     {
                 "chapters": [
                     "Living Christ"
                 ],
                 "title": "I Am He Who Liveth, I Am He Who Was Slain",
                 "begin": "March 29 2021",
                 "end": "April 4 2021",
                 "image": "https://assets.ldscdn.org/9d/cd/9dcd98c44afd0381f97655de08986f50aa9dd477/jesus_christ_prayer_rock.jpeg"
             },
        else:
            lesson = fetch_lesson_info(week, manual)

        if lesson is not None:
            lessons.append(lesson)

    print(json.dumps(lessons, indent=2))


main()
