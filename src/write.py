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
  if not os.path.exists('tmp.json'):
    return
  with open('tmp.json') as f:
    data = json.load(f)
  body = data['body']
  reporteds = [x['name'] for x in body]
  for student in data['students']:
    name = student['name']
    if name in reporteds:
      return
    body.append({'name': name, 'content': '自習'})

  with open(f'output/{datetime.now():%Y-%m-%d}.json', 'w') as f:
    json.dump(data, f, indent=2)
    os.remove('tmp.json')
