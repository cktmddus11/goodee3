'''
Created on 2020. 1. 20.

@author: GDJ_19
mariadb 사용하기
'''

import pymysql # pip install pymysql 실행하기
conn = pymysql.connect(host="localhost", port=3306, user="scott", passwd="1234", 
                       db="classdb", charset="utf8")

try:
    cur = conn.cursor()
    cur.execute("select * from item")
#    while true:
#       row = cur.fetchone() # 1건의 레코드만 조회
#       if row == none: # 읽을 레코드가 없음
#            break
#       print(row)
    for row in cur.fetchall():
        #print(type(row), row) 튜플
        print(row[0], row[1], row[2])
finally:
    cur.close()
    conn.close()