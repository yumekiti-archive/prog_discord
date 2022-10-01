import openpyxl
from datetime import datetime
import os
import shutil
import json

def init(fileName):
  shutil.copy('report.xlsx', fileName)

def main():
  fileName = f'output/{datetime.now().strftime("%Y_%m")}.xlsx'

  if not os.path.exists(fileName):
    init(fileName)

  book = openpyxl.load_workbook(fileName)
  sheet = book.active

  row = 8
  flag = True

  while flag:
    value = sheet.cell(row=row, column=1).value
    if value == None or value == '日付': flag = False
    else: row += 1

  with open('tmp.json', 'r') as f:
    data = json.load(f)
    sheet.cell(row=row, column=1).value = data.get('day')
    sheet.cell(row=row, column=3).value = data.get('body')
    sheet.cell(row=row, column=11).value = data.get('classroom')
    sheet.cell(row=row, column=14).value = len(data.get('students'))

  book.save(fileName)
