'''
Created on 2020. 2. 4.

@author: GDJ_19
numpy3.py : numpy 예제 : 배열 사본 생성, 재구조화 예제
'''
import numpy as np
# 0부터 9까지 임의의 남수 10개를 배열로 저장
x = np.random.randint(10, size = 10) # [0, 1, 2, 3, 4, 5, 6... 9]
x_sub = x[:2] # [0, 1]
print(x) 
print(x_sub) 
x_sub[0] = 20 # 사본(x_sub) 의 0번째 요소를 20으로 바꿈
print(x)
print(x_sub)
# 배열의 복사하기
x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

# 배열의 재구조 : 10개의 요소를 2차원 배열(5, 2) 로 재편성
x2 = x.reshape(5, 2)
print(x2)

# 0부터 9까지의 임의의 수를 9개 선택로 이루어진 배열을 생성하기
# 9개의 배열을 3행 3열배열로 재편성
y = np.random.randint(10, size = 9)
print(y)
y_sub = y.reshape(3, 3) # 9개이기 때문에 2, 5열 이런거는 불가능임
#!!! 재편성시 요소의 갯수가 맞아야함.
print(y_sub)


