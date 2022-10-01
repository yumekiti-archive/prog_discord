import attendance
import report
import os
from datetime import datetime

arg = os.sys.argv[1]

if arg == 'delete':
  attendance.delete()

if arg == 'report':
  fileName = f'output/{datetime.now().strftime("%Y_%m")}.xlsx'
  report.main(fileName)