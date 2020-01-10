
'''
Created on 2020. 1. 9.

@author: GDJ_19
'''


print("안녕하세요")
print("안녕하세요"[0])#0번 인덱스 문자 출력하기
print("안녕하세요"[4])
print("안녕하세요"[-1])
print("안녕하세요"[-2])


#부분 문자열

print("안녕하세요"[1:3])#1번 인덱스부터 2번인덱스까지 부분문자열출력
print("안녕하세요"[:3]) #0번 인덱스부터 2번인덱스까지 부분문자열출력
print("안녕하세요"[3:]) # 3번인덱스 부터 끝까지 부분문자열 출력
print("안녕하세요"[::2])# 2칸씩  건너서 찍음
print("안녕하세요"[::-1])# 역순으로 찍음
print("안녕하세요"[::-2])# 2칸씩역순으로 찍음

print(type("안녕하세요"))
print("'안녕하세요' 문자열길이:",len("안녕하세요"))

a = "helllllllllllllllllo"
cnt =0
for i in range(1,len(a)):
    if a[i]==("l"):
        cnt=cnt+1
print("l 문자의 갯수=",cnt)
print("l 문자의 갯수=",a.count('l'))
print("h 문자의 갯수=",a.count('h'))
print("l 문자의 위치=",a.find("l"))
print("a 문자의 위치=",a.find("a"))
print("l 문자의 위치=",a.index("l"))
print("a 문자의 위치=",a.index("a"))
