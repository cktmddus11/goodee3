'''
Created on 2020. 1. 21.

@author: GDJ_19
파일 읽기

open(파일이름, 파일모드, [인코딩 방식])

파일모드 
    "r" : 읽기 모드
    "w" : 쓰기 모드, 파일이 존재하지 않으면 파일을 생성해줌
    "r+" : 읽기/쓰기 겸용
    "a" : 쓰기모드. append 모드. 파일이 존재하지 않으면 파일을 생성해줌
                                            존재하는 경우는 기존 내용 이후에 추가됨
    "t" : 텍스트 모드. 기본형
    "b" : 이진모드
'''
infp = None
inStr = ""
infp = open("../0120/regularex3.py", "rt",  encoding='UTF8')
#                                                   text 파일 형테로 read해
while True:
    inStr = infp.readline()
    if inStr == None: # EOF(End Of File) 상태
        break
    print(inStr, end="") # 파일의 내용을 한줄씩 출력
infp.close()