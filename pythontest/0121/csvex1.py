'''
Created on 2020. 1. 21.

@author: GDJ_19
csv 파일 읽기
'''
import sys # command 라인에서 입력값 받기

# argv[0] 은 이 파일명이 들어감- c언어와 동일
input_file = sys.argv[1] # jeju1.csv
output_file = sys.argv[2] #jeju1_bak.csv
with open(input_file, 'r', newline="") as filereader: # filereader이 변수
# infp = open("../0120/regularex3.py", "rt",  encoding='UTF8') 과 동일
        with open(output_file, 'w', newline="") as filewriter:
            header = filereader.readline()
            header = header.strip() # 공백제거
            print(header) 
            header_list = header.split(",")
            print(header_list)
            filewriter.write(",".join(map(str, header_list))+"\r\n")
            # filewriter : filereader에서 읽은 원본 csv 파일의 헤더를
            # 문자열로 읽고 map으로 한후? 콤마로 묶어서 한줄 엔터(\r\n)해서 출력
            for row_list in filereader:
                filewriter.write("".join(map(str, row_list)))
                # rowlist 출력타입 str이기 때문에 그냥 print(row_list) 해도됨
