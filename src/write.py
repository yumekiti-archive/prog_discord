import os
import json
from datetime import datetime
import shutil

async def main(ctx, body, student):
  data = {
    'day': '{0:%d}'.format(datetime.now()),
    "classroom": 2302,
    "body": [],
    "students": [],
  }

  if not os.path.exists('tmp.json'):
    with open('tmp.json', 'w') as f:
      json.dump(data, f, indent=2)

  with open('tmp.json', 'r') as f:
    data = json.load(f)

  with open('tmp.json', 'w') as f:
    if body != []:
      data['body'].append(body)
      await ctx.send(f'{student.get("name")}さんが活動内容を記入しました。')
    if student not in data['students']:
      data['students'].append(student)
      await ctx.send(f'{student.get("name")}さんが出席しました。')
    json.dump(data, f, indent=2)

async def record():
  shutil.copy('tmp.json', f'output/{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}.json')
  if os.path.exists('tmp.json'):
    os.remove('tmp.json')
