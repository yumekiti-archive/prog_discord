import openpyxl
from datetime import datetime
import os
import shutil
import json

date = os.sys.argv[1]
if len(date) != 7:
  print('正しい形式で入力してください')
  print('例: 2021-01')
  exit()

def main():
  for file in os.listdir('output'):
    if date in file:
      print(file)

      fileName = f'output/{date}.xlsx'
      if not os.path.exists(fileName):
        shutil.copy('report.xlsx', fileName)

      book = openpyxl.load_workbook(fileName)
      sheet = book.active

      row = 8
      flag = True

      while flag:
        value = sheet.cell(row=row, column=1).value
        if value == None or value == '日付': flag = False
        else: row += 1

      with open(f'output/{file}', 'r') as f:
        data = json.load(f)

        sheet.cell(row=row, column=1).value = data.get('day')
        sheet.cell(row=row, column=3).value = data.get('body')[0].get('content')
        sheet.cell(row=row, column=11).value = data.get('classroom')
        sheet.cell(row=row, column=14).value = len(data.get('students'))

      book.save(fileName)

if __name__ == '__main__':
  main()