'''
Created on 2020. 1. 28.

@author: GDJ_19
xls 파일에 읽고 쓰기
'''

from xlrd import open_workbook
from xlwt import Workbook # pip install xlwt

input_file = "ssec1804.xls"
output_file  ="ssec1804out.xls"

output_workbook = Workbook() # 출력할 excel 파일
# add_sheet("전체") : sheet 추가
output_sheet = output_workbook.add_sheet("전체증감")
# workbook : excel 파일
with open_workbook(input_file) as workbook:
    # worksheet : ssec1804.xls 파일의 1.전체증감 sheet 를 선택
    worksheet = workbook.sheet_by_name("1.전체증감")
    for row_index in range(worksheet.nrows): # 선택된 sheet의 
        for column_index in range(worksheet.ncols): # 선택된
            output_sheet.write(row_index, column_index, # 선택
                               worksheet.cell_value(row_index, column_index))
            print(worksheet.cell_value
                  (row_index, column_index))
# output_sheet 를 worksheet를 output_file에 저장하기
output_workbook.save(output_file)