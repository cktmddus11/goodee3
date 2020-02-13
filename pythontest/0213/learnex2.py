'''
Created on 2020. 2. 13.

@author: GDJ_19
pandas 이용하기
'''
import pandas as pd
from sklearn import svm, metrics
xor_input = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
xor_df = pd.DataFrame(xor_input) # pandas 자료형 변환
xor_data = xor_df.loc[:,0:1] # 데이터
xor_label = xor_df.loc[:, 2] # 정답
clf = svm.SVC() # 사이킷런 객체. 머신러닝 툴
clf.fit(xor_data, xor_label) # 학습하기
pre = clf.predict(xor_data) # 평가실행. 답안지
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_score)
print("test 데이터로 평가하기")
test = [[0, 0], [1, 1], [1, 0], [0, 1], [1, 0], [1, 1]]
pre = clf.predict(test) # 평가실행. 답안지
ans = [0, 0, 1, 1, 1, 0]
ac_score = metrics.accuracy_score(ans, pre)
print("test 정답률=", ac_score)