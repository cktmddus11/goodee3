'''
Created on 2020. 1. 17.

@author: GDJ_19

dbex1.py : sqlite db 사용하기
'''

import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)
cur = conn.cursor() # SQL 구문 전달하는 객체
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
        name text unique,
        price integer );
    insert into items (name, price) values ('Apple', 800);
    insert into items (name, price) values ('Orange', 500);
    insert into items (name, price) values ('Banana', 300);
''')

conn.commit() # transaction 종료 - 테이블 생성, insert문 

cur = conn.cursor()
cur.execute("select * from items")
#cur.execute("select item_id, name, price from items")
item_list = cur.fetchall() # 모든 레코드 리턴
print(item_list) # 리턴타입 list 타입
for it in item_list:
    print(it)
