import openpyxl

def add_to_activity_report():
  book = openpyxl.load_workbook('report.xlsx')
  sheet = book.active

  i = 8
  flag = True

  while flag:
    value = sheet.cell(row=i, column=1).value
    if value == None or value == '日付': flag = False
    else: i += 1

  sheet.cell(row=i, column=1).value = 'Total'

  book.save('report.xlsx')

if __name__ == '__main__':
  add_to_activity_report()