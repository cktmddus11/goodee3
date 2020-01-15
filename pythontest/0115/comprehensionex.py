'''
Created on 2020. 1. 15.

@author: GDJ_19
컴프리헨션 예제

'''
numbers = []
for n in range(1, 11):
    numbers.append(n)
print(numbers)

print([x for x in range(1, 11)])

numlist = [x for x in range(1, 11)]
print(numlist)

# 1~ 10 까지 짝수리스트 생성
evenlist = []
for n in range(1, 11):
    if n % 2 == 0:
        evenlist.append(n)
print(evenlist)

evenlist = [x for x in range(1, 11) if x % 2 == 0 if x % 3 == 0]
print(evenlist)

# 중첩사용 컴프리헨션
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [x for row in matrix for x in row]
#              첫번째 행의        요소 한개한개를 가져와
print(list1)

# set 컴프리헨션
set1 = {x**2 for x in [1, 2, 3]}
print(set1)


# dictionary 컴프리헨션
id_name = {1:'차승연', 2:'ㅁㄴㄹㅇ', 3:'ㅎㅎㅎ'}
name_id = {val : key for key, val in id_name.items()}
print(name_id) #{'차승연': 1, 'ㅁㄴㄹㅇ': 2, 'ㅎㅎㅎ': 3}

# 1부터 10까지의 수중 짝수의 제곱을 출력하기 ; 컴프리헨션 문법 이용하기
#set2 = {x**2 for x in range(1, 11) if x % 2 == 0} # set 순서 유지 X, 종복되지 않음 
# set2 = [x**2 for x in range(1, 11) if x % 2 == 0] # 리스트 순서 유지
set2 = {x**2 for x in range(1, 11) if x % 2 == 0}
print(sorted(set2)) #sorted를 하면 set이었던걸 자동으로 list로 바꿈?








