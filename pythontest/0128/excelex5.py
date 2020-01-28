'''
Created on 2020. 1. 28.

@author: GDJ_19
문제 : ssec1804.xls 파일에서 "1. 남자", "2. 여자" sheet 를 선택하여
남자, 여자 ssec1804mf.xls로 저장하기
'''
from xlrd import open_workbook
from xlwt import Workbook # pip install xlwt

input_file = "ssec1804.xls"
output_file  ="ssec1804mf.xls"

output_workbook = Workbook() # 출력할 excel 파일
# add_sheet("전체") : sheet 추가
# 1. workbook에 두개의 sheet만듦
output_sheet_male = output_workbook.add_sheet("남자")
output_sheet_female = output_workbook.add_sheet("여자")


# 원본 파일의 남자, 여자 sheet를 읽어온 값 worksheet에 저장함
# worksheet에 있는 행, 열 읽엉서 output_sheet에 내용 저장
def makesheet(output_sheet):
    for row_index in range(worksheet.nrows): # 선택된 sheet의 
        for column_index in range(worksheet.ncols): # 선택된
            output_sheet.write(row_index, column_index, # 선택
                               worksheet.cell_value(row_index, column_index))
            print(worksheet.cell_value
                  (row_index, column_index))         


# workbook : excel 파일
with open_workbook(input_file) as workbook:
    # worksheet : ssec1804.xls 파일의 1.전체증감 sheet 를 선택
    worksheet= workbook.sheet_by_name("1.남자")    
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)

# output_sheet 를 worksheet를 output_file에 저장하기
output_workbook.save(output_file)