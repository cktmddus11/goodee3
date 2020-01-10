'''
Created on 2020. 1. 10.

@author: GDJ_19
'''

import operator

dic, list = {}, []
dic = {"Thomas" : "토마스", "Edward" : "에드워드", "Henry" : "헨리"
       , "Gothen":"고든", "James" : "제임스"}
list = sorted(dic.items(), key = operator.itemgetter(0), reverse=True) # 기본값 reverse = False 
# 영문operator.itemgetter(0)순으로 역순으로 정렬
#                                      1 로 하면 한글 순으로 
print(list)
