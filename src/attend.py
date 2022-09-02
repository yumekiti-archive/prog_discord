import os
import json
from datetime import datetime

async def add():
  data = {
    'day': '{0:%d}'.format(datetime.now()),
    "classroom": "2200",
    "body": "This is a test message",
    "students": [],
  }
  student = {
    "name": "John Doe",
    "year": "1",
  }

  if not os.path.exists('tmp.json'):
    with open('tmp.json', 'w') as f:
      json.dump(data, f, indent=2)

  with open('tmp.json', 'r') as f:
    data = json.load(f)

  data['students'].append(student)

  with open('tmp.json', 'w') as f:
    json.dump(data, f, indent=2)

async def delete():
  if os.path.exists('tmp.json'):
    os.remove('tmp.json')

if __name__ == '__main__':
  import asyncio
  asyncio.run(add())