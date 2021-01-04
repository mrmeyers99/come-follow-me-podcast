# coding=utf8

books = [
    {"name": "Doctrine and Covenants", "chapters": 138},
]

print('    "The Articles of Faith and Official Declarations 1 and 2": [\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-doctrine-and-covenants/2015-11-1390-official-declaration-1-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-doctrine-and-covenants/2015-11-1400-official-declaration-2-male-voice-64k-eng.mp3?lang=eng&download=true",\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-pearl-of-great-price/2015-11-0160-the-articles-of-faith-male-voice-64k-eng.mp3?lang=eng&download=true"\n' +
      '    ],')
print('    "The Family: A Proclamation to the World": [\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/06897family001/06897_2011-01-0000-the-family-a-proclamation-to-the-world-64k-eng.mp3?lang=eng&download=true"\n' +
      '    ],')
print('    "Joseph Smith - History": [\n' +
      '      "https://media2.ldscdn.org/assets/scriptures/the-pearl-of-great-price/2015-11-0150-joseph-smith-history-male-voice-64k-eng.mp3?lang=eng&download=true"\n' +
      '    ],')

x = 0

for book in books:

    for chapter in range(1, book['chapters'] + 1):
        x += 1
        # https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0010-1-nephi-01-male-voice-64k-eng.mp3?lang=eng&download=true
        # https://media2.ldscdn.org/assets/scriptures/the-book-of-mormon-another-testament-of-jesus-christ/2015-11-0660-words-of-mormon-01-male-voice-64k-eng.mp3?lang=eng&download=true
        print('    "' + book['name'] + ' ' + str(chapter)
              + '": ["https://media2.ldscdn.org/assets/scriptures/the-doctrine-and-covenants/2015-11-'
              + ('%03d' % x) + '0'
              + '-section'
              + '-' + ('%02d' % chapter)
              + '-male-voice-64k-eng.mp3?download=true"],')
