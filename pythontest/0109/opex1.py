'''
Created on 2020. 1. 9.

@author: GDJ_19
'''
num1 = int(input("첫번쨰 정수 입력 : "))
num2 = int(input("두번쨰 정수 입력 : "))
print(num1, "+", num2,"=",(num1 + num2))
print(num1, "-", num2,"=",(num1 - num2))
print(num1, "*", num2,"=",(num1 * num2))
print(num1, "/", num2,"=",(num1 / num2)) # 1.5 
print(num1, "//", num2,"=",(num1 // num2)) # 1
print(num1, "%", num2,"=",(num1 % num2))
print(num1, "**", num2,"=",(num1 ** num2))

print("a"+"b"+"c")
print("abc"*3) # 문자열 3번 출력

# 있는 그대로 문자열 출력 + 로 문자열 연결하는거랑 똑같
# print(''' ~ ''') 큰 따옴표 작은 따옴표 구별안함
print("""안녕하세요, 홍길동이니다. 반갑습니다. 어쩌구 저쩌구.....
    넝린얼ㄴ이ㅏㅓㄹ이나런;ㅇㄹㄴ""")