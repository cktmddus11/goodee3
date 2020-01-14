'''
Created on 2020. 1. 14.

@author: GDJ_19
예외 처리 예제
'''
mystr = "파이썬 공부 중입니다. 열심히 파이썬을 공부합시다"
strpos = []  # 파이썬 문자의 위치저장
index = 0
while True:
    try:
        # index 이후의 파이썬 문자열의 위치
        index = mystr.index("파이썬", index)  # 0번쨰 인덱스 이후의 값에서 파이썬 찾기
        print(index)
        strpos.append(index)
        index += 1
    except:
        break
print("파이썬 문자의 위치 : ", strpos, "문자 갯수 : ", len(strpos))
