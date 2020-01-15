'''
Created on 2020. 1. 14.

@author: GDJ_19

리스트의 각각의 요소를 변경
'''

before = ["2019", "07", "15"]
print(type(before[0]))
after = list(map(int, before)) # 리스트에 있는 문자열을 int로 각각변환하여 리스트로 만듦
print(type(after[0]))
num = int("100") + 1
print(num)


mylist = [1, 2, 3, 4, 5]
# map을 이용하여 mylist 각각의 값에 10을 더하기
add = lambda num:num+10
myList = list(map(add, mylist)) # 각각의 값을 add함수를 이용하여 처리한 후 리스트로 만듦
print(myList)

list1 = [1, 2, 3,4]
list2 = [10, 20, 30, 40]
#haplist 리스트에 list1과 list2 각각 더한값을 저장하기
"""
haplist = []
for i in range(len(list1)):
        haplist.append(list1[i] + list2[i])
print(haplist)"""

hap = lambda num1, num2 : num1 + num2

"""for i in range(len(list1)):
    haplist.append(hap(list1[i],list2[i]))
print(haplist)"""

haplist = list(map(hap, list1, list2))
haplist = list(map(lambda num1, num2 : num1 + num2, list1, list2))
print(haplist)






