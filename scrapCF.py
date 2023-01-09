import requests
import xlsxwriter
import os
from bs4 import BeautifulSoup as bs

response = requests.get('https://codeforces.com/submissions/naveenkant227/page/1')

soup = bs(response.text, 'html.parser')

mainBody = soup.find('table', {'class' : 'status-frame-datatable'})

records = mainBody.findAll('tr')
records = iter(records)
next(records)

workbook = xlsxwriter.Workbook('SubmissionsRecord.xlsx')

cell_format = workbook.add_format()
cell_format.set_align('left')

worksheet = workbook.add_worksheet()



worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 45)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 30)
worksheet.set_column('F:G', 15)

titles = ['Submission ID',
		'When',
		'Problem',
		'Language',
		'Verdict',
		'Time',
		'Memory']

for cl in range(7):	
	worksheet.write(0, cl, titles[cl])

rw = 1
for row in records:

	data = row.findAll('td')
	dataList = []

	for column in data:
		dataList.append(column.text.split())

	col = 0
	worksheet.write(rw, col, int(dataList[0][0]), cell_format)
	worksheet.write(rw, col+1, dataList[1][0])
	worksheet.write(rw, col+2, ' '.join(dataList[3]))
	worksheet.write(rw, col+3, ' '.join(dataList[4]))
	worksheet.write(rw, col+4, ' '.join(dataList[5]))
	worksheet.write(rw, col+5, ' '.join(dataList[6]))
	worksheet.write(rw, col+6, ' '.join(dataList[7]))
	rw += 1


workbook.close()
os.startfile('D:\Code\Projects\PythonApp\Web Scraping\projects\SubmissionsRecord.xlsx')
	