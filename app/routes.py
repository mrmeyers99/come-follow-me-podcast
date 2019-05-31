from app import app
from datetime import datetime

from app.client import Client


@app.route('/')
@app.route('/index')
def index():
    current_week = int(datetime.today().strftime("%V")) - 1

    client = Client()
    client.get_episodes_for_week(current_week)
    return "Hello, World!"
