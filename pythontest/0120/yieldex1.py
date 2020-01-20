'''
Created on 2020. 1. 20.

@author: GDJ_19
yieldex1 : 함수의 종료없이 yield예약어로 값 리턴
'''
def genFun(num):
    for i in range(10, num + 10):
        yield(i) # 함수를 호출한 곳에 i값을 전달함
        # 함수가 끝나지 않아도 값을 계속 전달해줌
        print(i, "값 반환")
#print(genFun(5)) # <generator object getFun at 0x00AD9178>
# type(genFun) generator 타입, 그 자체가 저장공간이 됨
#print(list(genFun(5)))
            # getFun : 하나씩값을 저장하고있음
            
for i in list(genFun(5)):
    print(i)