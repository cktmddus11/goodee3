'''
Created on 2020. 1. 9.

@author: GDJ_19

금액을 입력받아 동전으로 바꿔주는 프로그램 작성하기
단 동전은 500, 100, 50,10, 1 의 종류가 있다.
각각 동전의 갯수를 출력하기. 동전의 갯수는 최소개로 출력한다. 

'''
money = int(input("금액을 입력하세요"))
#3650
#
fivehun = (money // 500)
money = money % 500
print("500원의 동전 갯수 :",fivehun)

onehun = (money // 100)
money = money % 100
print("100원의 동전 갯수 :",onehun)

fiveten = (money // 50) 
money = money % 50
print("50원의 동전 갯수 :",fiveten)

ten = (money // 10) 
money = money % 10
print("10원의 동전 갯수 :",ten)


print("1원의 동전 갯수 :",money)

#print(fivehun, money)

