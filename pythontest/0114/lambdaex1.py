'''
Created on 2020. 1. 14.

@author: GDJ_19
람다식으로 함수 구현하기
'''
def hap(num1, num2):
    res = num1 + num2
    return res

print(hap(10, 20))

hap2 = lambda num1, num2:num1 + num2
print(hap2(10, 20))

hap2 = lambda num1, num2:num1 * num2
print(hap2(10, 20))

# 매개변수에 기본값 설정하기
hap3 = lambda num1= 0, num2=1 : num1 + num2
print(hap3())
print(hap3(100))
print(hap3(100, 200))