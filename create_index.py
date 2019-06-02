# coding=utf8

books = [
    {"name": "Moses", "chapters": 8},
    {"name": "Abraham", "chapters": 5},
    {"name": "Joseph Smith—Matthew", "chapters": 1},
    {"name": "Joseph Smith—History", "chapters": 1}
]

x = 0

for book in books:
    for chapter in range(1, book['chapters'] + 1):
        x += 1
        # https://media2.ldscdn.org/assets/scriptures/the-new-testament/2015-11-0010-matthew-01-male-voice-64k-eng.mp3?download=true
        # https://media2.ldscdn.org/assets/scriptures/the-new-testament/2015-11-0290-mark-01-male-voice-64k-eng.mp3?download=true
        # https://media2.ldscdn.org/assets/scriptures/the-new-testament/2015-11-2600-revelation-22-male-voice-64k-eng.mp3?download=true
        print('    "' + book['name'] + ' ' + str(chapter)
              + '": "https://media2.ldscdn.org/assets/scriptures/the-pearl-of-great-price/2015-11-'
              + ('%03d' % x) + '0'
              + '-' + book['name'].lower().replace(' ', '-').replace('—', '-')
              + ('-' + ('%02d' % chapter) if book['chapters'] > 1 else '')
              + '-male-voice-64k-eng.mp3?download=true",')
