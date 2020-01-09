'''
Created on 2020. 1. 9.

@author: GDJ_19

input(), print() 함수
input("입력전 출력 문자열") 함수는 기본적으로 문자열을 입력받는다.
print(출력값1, 출력값2...) 함수는 여러개 출력시  ,로 연결가능하다.

'''

a = int(input("값1 입력"))
b = int(input("값2 입력"))
result = a + b
print(a ,"+",b,"=",result)

print("%d + %d = %d" % (a, b, result))
print("안녕하세요", end="") # end는 기본으로 \n 라는 줄바꿈 문자로 되어있음
# : 넣으면 가로로 나오면서 : 찍힘
print("홍길동입니다.")


#format 함수를 이용하기
print("{0:d} {1:5d} {2:05d}".format(100, 200, 300)) #100   200 00300
print("{2:d} {1:5d} {0:05d}".format(100, 200, 300)) #300   200 00100