'''
Created on 2020. 1. 10.

@author: GDJ_19
전역 변수 사용하기
'''
from inspect import formatargvalues
def func1():
    global gval # 이거 하면 전역 변수로 사용가능
    gval = 200 # 지역 변수
    a = 20 # 지역변수 -> 함수내에서만 사용가능
    b = 1000
    print("func1() 함수 호출됨", gval, a)

def func2():
    print("func2() 함수에서 func1() 함수를 호출함")
    func1()
    b = 2000 # 지역변수
    print("전역 변수 gval 값=", gval, a, b)


gval = 100 #전역변수 => 모든 함수에서 사용이 가능한 변수
a = 10 
if __name__ == '__main__': # 명시적으로 프로그램 시작을 표시
    func2()