'''
Created on 2020. 1. 10.

@author: GDJ_19

리스트 예제
     파이썬 : 리스트(자바의 배열, list) => [],
                딕셔너리(자바의 Map) => {},
                튜플(상수처리된 리스트) => (),

'''

a = [0, 0, 0, 0]
b = []

suma, sumb = 0, 0
for i in range(0, len(a)):
    a[i] = int(input(str(i + 1) +"번째 값 : ")) # 0으로 초기화 되어있는 리스트에 입력한 값을 하나씩 대입
    suma += a[i]
    b.append(a[i]) # 리스트에 입력한 값 하나씩 추가
    sumb += a[i]
    
    
print("리스트 a : ", a)
print("리스트 b : ", b, "리스트 b 길이 : ", len(b))
print("a 리스트 합계 : ", suma)
print("b 리스트 합계 : ", sumb)
