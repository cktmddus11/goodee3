'''
Created on 2020. 1. 10.

@author: GDJ_19

aa, bb 배열을 생성하고
aa 배열은 0 부터 짝수 100개를 저장하고
bb 배열은 aa배열의 역순으로 값을 저장하기
aa[0] ~ aa[9], bb[99] ~ bb[90]
'''

# 리스트 생성 - 빈 리스트이므로 a[i] = 값 이거 안됨 -> append사용
aa = []
bb = []

# aa리스트에 0부터 짝수 100개 저장
b = 0 # 리스트에 넣을 값 초기화 
for i in range(0, 100):
    aa.append(b) # aa리스트에 값 저장
    b = b + 2 
     
# bb 리스트에 aa리스트 역순으로 값 저장
for i in range(99, -1, -1):
    bb.append(aa[i])
    

for i in range(0, 10):
    print("aa[%d] = %d,%2s" %(i, aa[i], " "), end="")
print()
for i in range(99, 89, -1): # -1, -11, -1
    print("bb[%d] = %d,%5s" %(i, bb[i], " "), end = "")

    