import openpyxl
from datetime import datetime
import os
import shutil
import json

def init(fileName):
  shutil.copy('report.xlsx', fileName)

def add_to_activity_report():
  fileName = f'output/{datetime.now().strftime("%Y_%m")}.xlsx'

  if not os.path.exists(fileName):
    init(fileName)

  book = openpyxl.load_workbook(fileName)
  sheet = book.active

  i = 8
  flag = True

  while flag:
    value = sheet.cell(row=i, column=1).value
    if value == None or value == '日付': flag = False
    else: i += 1

  with open('tmp.json', 'r') as f:
    data = json.load(f)
    sheet.cell(row=i, column=1).value = data.get('day')

  book.save(fileName)

if __name__ == '__main__':
  add_to_activity_report()