'''
Created on 2020. 1. 22.

@author: GDJ_19

excelex1.py : xlsx 파일 읽기 excel 파일 읽기

xlxs : pip install openpyxl
xls : pip install xlrd
'''
import openpyxl # pip install openpyxl

filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0] # 첫 번째 sheet 선택
data = []
for row in sheet.rows:
    line = []
    for l, d in enumerate(row):
        # i :  열의 번호, d : 데이터
        line.append(d.value) # 한 줄의 셀의 값을 list로 저장
        # print(l, end="\t")
    print(line)
    data.append(line)
print(type(data))
print(data)

# enumerate : 리스트에서 데이터와 index값을 제공
for i, a in enumerate(data): # i : index, a : data
    if(i >= 10):
        break;
    print(i + 1, a)
