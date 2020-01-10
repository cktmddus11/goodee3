'''
Created on 2020. 1. 10.

@author: GDJ_19

배열의 값의 합과 평균을 구하는 함수 작성하기 
'''



def getSum(numlist):
    # 역슬래시 : 원래 한줄인데 두줄로 쓰려고 연결문자 역할인거
    return sum(numlist) / len(numlist)  \
        if len(numlist) > 0 else 0 
        
    """if len(numlist > 0) > 0:
        return sum(numlist) / len(numlist)
    else:
        return 0:"""

def getMean(numlist):
    return sum(numlist)

list = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8]    
print("list의 값의 합 : ", getSum(list))
print("list의 값의 평균 : ", getMean(list))

list2 = []
print("list의 값의 합 : ", getSum(list2))
print("list의 값의 평균 : ", getMean(list2))


tp = (2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8) # 튜플
print("tp의 값의 합 : ", getSum(tp))
print("tp의 값의 평균 : ", getMean(tp))





