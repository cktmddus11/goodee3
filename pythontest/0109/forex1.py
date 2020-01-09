'''
Created on 2020. 1. 9.

@author: GDJ_19
구구단 출력
'''

i, j = 0, 0
for i in range(2, 10):
    print("{0:4d}".format(i),"단") # print("%5d" % i)
    for j in range(2, 10):
        print(i, "X", j,"=", i * j)
    print()    

print("===========")
for i in range(2, 10):
    print("\t%d단\t"%i, end="") #print("%5d단%15s" % (i, " "), end="")
print()
for i in range(2, 10):
    for j in range(2, 10):
        print("{0:2d} X {1:2d} = {2:2d}".format(j, i, j * i), "\t", end="")
        # print("%2d X %2d = %3d " % (i, j, (i * j)), end="")
    print()