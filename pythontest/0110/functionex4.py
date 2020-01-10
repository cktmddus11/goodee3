'''
Created on 2020. 1. 10.

@author: GDJ_19

1. 리턴값 두개 반환하기 : 리스트로 반환
2. 가변 매개변수 함수 정의 

** 자바
Collection : 객체의 모음
- list : 순서 유지 (ArrayList, #Vector, LinkedList)
- set  : 중복 X (HashSet, TreeSet)
Map : (key, value)의 모음 (HashMap, TreeMap, #HashTable)

(#은 예전꺼)

**파이썬 
자바의 list -> list, tuple [], ()
자바의 Map -> dictionary {}
'''


def multi(num1, num2):
    #return num1 + num2, num1 - num2
    list = []
    res1 = num1 + num2
    res2 = num1 - num2
    list.append(res1)
    list.append(res2)
    return list

def paramFunc(* p): # 0개이상 매개변수
    result = 0;
    for i in p:
        result += i
    return result

list = []
hap, sub = 0, 0
list = multi(100, 200)
hap = list[0]
sub = list[1]


print("multi 함수의 리턴값 : %d, %d "%(hap, sub))
# 가변 파라미터 연습
print("paramFunc(10, 20) =", paramFunc(10, 20))
print("paramFunc(10, 20, 30) =", paramFunc(10, 20, 30))
