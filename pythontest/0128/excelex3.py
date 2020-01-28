'''
Created on 2020. 1. 28.

@author: GDJ_19
xls 파일 읽기
xls : pip install xlrd
'''

from xlrd import open_workbook

input_file = "ssec1804.xls"
workbook = open_workbook(input_file)

print("worksheets 의 갯수 : ", workbook.nsheets)
for worksheet in workbook.sheets():
    print("worksheet 이름 : ", worksheet.name, "\n행수 : ", worksheet.nrows, "\n컬럼수 : ", worksheet.ncols)
