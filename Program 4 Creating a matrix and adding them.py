#Write a program to create 2 matrices of 3x4 and print their sum.
import numpy as np
a=list(input(""))
b=list(input(""))
c=list(input(""))
A=[a,b,c]
print(A)

a=list(input(""))
b=list(input(""))
c=list(input(""))
B=[a,b,c]
print(B)
slist=np.zeros((3,3))
for x in range(len(A)):
    for y in range(len(B)):
        slist[x][y]=A[x][y]+B[x][y]
print(slist)