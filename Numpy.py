# -*- coding: utf-8 -*-
"""
Created on Sun May 19 02:34:23 2019

@author: Kamran Hashmi
"""

import numpy as np
'''x=np.array([[1,2,3],[7,8,9]])
y=np.array([[4,5,6],[10,11,12]])
print(y)
print(x*y)

a=np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])
b=[1,2,3,10],[4,5,6,11],[7,8,9,12]
c=a[:3, 2:4]
d=b[:3, 2:4]
print(c)
print(d)
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array([0,1,0,1])
print(b)
print(a[np.arange(4),b])
jagga=(a%3!=0)
print(a[jagga])
'''
x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
v=np.array([1,2,3,4])
y=np.empty_like(x)
for i in range(3):
    y[i,:]=x[i,:]+v
print(y)

z=x+v
print(z)