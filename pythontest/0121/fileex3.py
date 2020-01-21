'''
Created on 2020. 1. 21.

@author: GDJ_19
파일 존재 여부 확인하기
'''

import os.path
file = 'c:\\Data\\Python\\nofile.txt'
file = "csvex1.py"
file = "../0120"
file = "../01200"

if os.path.isfile(file):
    print("Yes. it is a file")
elif os.path.isdir(file):
    print("Yes.it is a directory")

if os.path.exists(file):
    print("Something exist")
else:
    print("Nothing")
