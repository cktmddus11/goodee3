'''
Created on 2020. 1. 14.

@author: GDJ_19

피보나치 수열 구하기
피보나치 수열 : 0, 1, 1, 2, 3, 5, 8, 13, 21...
입력값 : 5
0, 1, 1, 2, 3
입력값 : 10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

0 1 1 2 
    
'''

def fibo(n):
    global num1, num2, num3 # 1. 이게없으면
    # fibolist = [] 지역변수이므로 함수 밖에서 사용불가
    fibolist.append(num1) # 2. 지역변수로 함수내에 num1이 있는지 찾게됨 
    fibolist.append(num2) # 근데 없으니까 에러가 나는거임
    fibolist.append(num3)
    for i in range(3, n): # 0 1 1 2 3
        num1 = num2  # 1  -> 1  
        num2 = num3  #  1 -> 2 
        num3 = num1 + num2 # 2 -> 3
        fibolist.append(num3)



fibolist = [] # 전역변수 
num1 = 0
num2 = 1
num3 = num1 + num2
num = int(input("피보나치 수열을 구할 갯수를 입력하세요. 단 3이상의 값"))
print("f(",num, ")=", end="")
fibo(num)
print(fibolist)
