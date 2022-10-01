import os
import json

async def main(now, body, classroom, student):
  data = {
    'day': '{0:%d}'.format(now),
    "classroom": classroom,
    "body": "",
    "students": [],
  }

  if not os.path.exists('tmp.json'):
    with open('tmp.json', 'w') as f:
      json.dump(data, f, indent=2)

  with open('tmp.json', 'r') as f:
    data = json.load(f)

  data['students'].append(student)

  with open('tmp.json', 'w') as f:
    if body != []:
      data['body'].append(body)
    data['students'] = list({v['name']:v for v in data['students']}.values())
    json.dump(data, f, indent=2)

async def delete():
  if os.path.exists('tmp.json'):
    os.remove('tmp.json')
