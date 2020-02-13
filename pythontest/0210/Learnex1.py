'''
Created on 2020. 2. 10.

@author: GDJ_19
머신러닝 예제. 사이킷런 툴 사용하기
'''

from sklearn import svm # pip install sklearn

xor_data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
data = [] #샘플 데이터
label = [] # 결과값
# 샘플데이터 생성
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q]) # 문제와 
    label.append(r) # 결과 분리
    
clf = svm.SVC() # 머신러닝을 위한 객체
clf.fit(data, label) # 기계를 학습시킴

# 평가하기 위한 데이터 생성
sample_data = [[1, 1], [1, 0], [0, 1], [1, 1], [1, 0], [0, 0]]
# 평가하기.pre  : 예측되는 결과. 답안지
pre = clf.predict(sample_data)
ans = [0, 1, 1, 0, 1, 0] # 정답지
print("예측 결과 :",pre)
ok = 0
total = 0
for idx, answer in enumerate(ans):
    p = pre[idx]
    if p == answer:
        ok +=1
    total += 1
print("정답률 ", ok, "/", total, "=", ok/total)




