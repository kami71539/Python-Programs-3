# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:08:11 2019

@author: Kamran
"""

r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
mat=[ ]

for i in range(r):
    mat.append([])
    for j in range(c):
        x=int(input("Enter the element"))
        mat[i].append(x)
print(mat)