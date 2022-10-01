import os
import json

async def main(ctx, now, body, classroom, student):
  data = {
    'day': '{0:%d}'.format(now),
    "classroom": classroom,
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

async def delete():
  if os.path.exists('tmp.json'):
    os.remove('tmp.json')
