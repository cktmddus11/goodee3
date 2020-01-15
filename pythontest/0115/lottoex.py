'''
Created on 2020. 1. 15.

@author: GDJ_19

로또 번호 생성기
'''
import random
def getNumber():
    return random.randrange(1, 46)
lotto = set()
for i in range(0, 7):
    lotto.add(getNumber())
print("추첨된 로또 번호 =>", sorted(lotto))
