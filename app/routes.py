from app import app
from datetime import datetime

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
