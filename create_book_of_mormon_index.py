# coding=utf8

books = [
    {"name": "1 Nephi", "chapters": 22},
    {"name": "2 Nephi", "chapters": 33},
    {"name": "Jacob", "chapters": 7},
    {"name": "Enos", "chapters": 1},
    {"name": "Jarom", "chapters": 1},
    {"name": "Omni", "chapters": 1},
    {"name": "Words of Mormon", "chapters": 1},
    {"name": "Mosiah", "chapters": 29},
    {"name": "Alma", "chapters": 63},
    {"name": "Helaman", "chapters": 16},
    {"name": "3 Nephi", "chapters": 30},
    {"name": "4 Nephi", "chapters": 1},
    {"name": "Mormon", "chapters": 9},
    {"name": "Ether", "chapters": 15},
    {"name": "Moroni", "chapters": 10},
]

print('    "Introductory Pages of the Book of Mormon": [\n' +
      '      "http://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0002-traditional-title-page-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0003-introduction-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0004-the-testimony-of-three-witnesses-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0005-the-testimony-of-eight-witnesses-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0006-testimony-of-the-prophet-joseph-smith-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0007-a-brief-explanation-about-the-book-of-mormon-male-voice-64k-eng.mp3?lang=eng&download=true"\n' +
      '    ],')

x = 0

for book in books:

    for chapter in range(1, book['chapters'] + 1):
        x += 1
        # https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0010-1-nephi-01-male-voice-64k-eng.mp3?lang=eng&download=true
        # https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0660-words-of-mormon-01-male-voice-64k-eng.mp3?lang=eng&download=true
        print('    "' + book['name'] + ' ' + str(chapter)
              + '": ["https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-'
              + ('%03d' % x) + '0'
              + '-' + book['name'].lower().replace(' ', '-').replace('—', '-')
              + '-' + ('%02d' % chapter)
              + '-male-voice-64k-eng.mp3?download=true"],')
