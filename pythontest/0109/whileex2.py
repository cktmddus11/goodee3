'''
Created on 2020. 1. 9.

@author: GDJ_19

랜덤 함수를 사용하여 숫자 맞추기
    컴퓨터가 1부터 99까지 임의의 수를 저장하고, 
    화면에 숫자를 입력받아 컴퓨터가 저장한 수를 맞추기. 
    -입력된 수가 저장된 수보다 크면 작은 수를 입력하세요
    -입력수가 저장된 수보다 작으면 더 큰 수 를 입력하세요  메시지 출력하기
    저장된 수와 입력된 수가 같은 경우, 입력건수를 화면에 출력하고 프로그램 종료
'''
import random

rnum = random.randrange(1, 100) # 1부터 99 까지의 임의의  수
i = 0
# True : boolean타입의 예악어, False
while True:
    a = int(input("숫자를 입력하세요 : "))
    if a > rnum : 
        print("작은 수 입니다.")
    elif a < rnum: 
        print("큰 수 입니다.")
    if a == rnum: # else
        print("정답입니다")
        break
    i = i + 1
print("%d번 만에 맞췄습니다."%i)    

