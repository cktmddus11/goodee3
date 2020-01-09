'''
Created on 2020. 1. 9.

@author: GDJ_19
'''
height = int(input("삼각형의 높이를 입력하세요"))
"""for i in range(1, height+1):
    for j in range(1, i+1):
        print("*", end="")
    print()"""
    
    
for i in range(1, height+1):
    print("*"*i)
    
print()

for i in range(height, 0, -1):
    print("*"*i)
    
    
print()

for i in range(1, height+1):
    print(" "*(height -i), end="")
    print("*"*i)

print("정삼각형")
for i in range(1, height+1):
    print(" "*(height -i), end="")
    print("*"*(i*2-1))


print("정역삼각형")
for i in range(1, height+1):
    print(" "*(i-1), end="")
    print("*"*(((height-i)*2)+1))
print()    



