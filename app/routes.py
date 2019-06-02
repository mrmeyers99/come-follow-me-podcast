from app import app
from datetime import datetime
import json

from app.client import Client


@app.route('/')
@app.route('/index')
def index():
    current_week = int(datetime.today().strftime("%V")) - 1

    client = Client()
    lesson = client.get_lesson_for_week(current_week)

    info = ""
    for chapter in lesson['chapters']:
        info += chapter['name'] + ' ' + chapter['url'] + "<br>"
    return info


@app.route('/urls')
def urls():
    d2 = json.load(open("book_urls.json"))
    return json.dumps(d2)
