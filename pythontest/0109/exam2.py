'''
Created on 2020. 1. 9.

@author: GDJ_19

초를 입력받아 몇시간 몇분 몇초인지 출력하기

'''

time = int(input("초을 입력하세요"))
hour = (time // 3600)
time = time % 3600
min = (time // 60)
time = time % 60

print(hour, "시간", min, "분", time,"초")


