'''
Created on 2020. 1. 9.

@author: GDJ_19

exam3.py : 숫자를 입력받아 입력수까지 합을 출력하기
 숫자를 입력받아 입력수까지 짝수 합을 출력하기
'''

num = int(input("숫자를 입력하세요"))
sum = 0
for i in range(1, num+1):
    sum += i
    
print(sum)


print("홀수의 합 ", end=":")
sum = 0
for i in range(1, num+1, 2):
    sum += i
    
print(sum)

print("짝수의 합 ", end=":")
sum = 0
for i in range(0, num+1, 2):
    sum += i
    
print(sum)



