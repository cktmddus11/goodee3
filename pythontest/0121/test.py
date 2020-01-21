'''
Created on 2020. 1. 21.

@author: GDJ_19
'''
import codecs
filename = "jeju1.csv"
csv = codecs.open(filename, "r", "euc-kr").read()
outfp = None
outfp = open("jeju1.txt", "w", encoding="utf8")
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "" :
        continue #입력 줄 공백
    cells = row.split(",")
    data.append(cells)
for c in data:
    outfp.write(" ".join(c)+"\n")
    #               리스트를 문자열로
    # outfp.write(" ".join(map(str,c)) +"\n")