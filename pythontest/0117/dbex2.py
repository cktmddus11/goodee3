'''
Created on 2020. 1. 17.

@author: GDJ_19
dbex2.py : 화면에서 내용을 입력받아 sqlite db에 내용 저장하기
'''

import sqlite3

dbpath = "test.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.executescript('''
    drop table if exists usertable;
    create table usertable (userid varchar(15) primary key,
        username varchar(20), 
        email varchar(30) unique, 
        year integer );
''')
con.commit()

cur = con.cursor()
while True:
    data1 = input("사용자 ID =>")
    if data1 == '':
        break
    data2 = input("사용자 이름 =>")
    data3 = input("이메일 =>")
    data4 = input("출생 연도 =>")
    sql = "insert into usertable values ('"+data1+"', '"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    con.commit()
#등록된 내용 select 로 조회하기

cur = con.cursor()
cur.execute("select *from usertable")
user_list = cur.fetchall()
print(user_list)
for u in user_list:
    print(u)

con.close()


