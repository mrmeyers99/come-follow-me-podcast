# coding=utf8

from app.client import Client
from datetime import datetime

client = Client()

# for i in range(1, 52):
print(client.get_lesson_for_date(datetime.strptime('December 30 2019', '%B %d %Y')))
