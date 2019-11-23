# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:45:52 2019

@author: Kamran Hashmi
"""

import numpy as np
#a=np.array([(1,2,3),(4,5,6)])
#print(a)
#
import time

import sys

#s=range(1000)
#print(sys.getsizeof(10)*len(s))
#d=np.arange(1000)
#print(d.size*d.itemsize)
#numpy is faster takes less space and is super convenient when compared with lists.



#size=5
#l1=range(size)
#l2=range(size)
#
#a1=np.arange(size)
#a2=np.arange(size)
#
#start=time.time()
#result=[(x,y) for x,y in zip(l1,l2)]
#print((time.time()-start)*1000)
#print(result,"of list")
#start=time.time()
#result=a1+a2
#print((time.time()-start)*1000)
#print(result,"of array")
#
a=np.array([(1,2),(3,4),(5,6)])
b=np.array([(12,11),(10,9),(8,7)])
#print(a.ndim) #Calculating dimensions of an array.
#print(a)
#print(a.itemsize)   to find how many byte size does th eitem of array contains
#print(a.dtype)  To find the type of items in the array
#print(a.size) To find how many elements are stored in an array.
#print(a.shape) To find how many rows and columns the matrix has.
print(a)
#a=a.reshape(2,3)
#print(a)
#print(a[0:,0])
#print(a[0:2,1])
#a=np.linspace(1,2,10)
#print(a.max())
#print(a.min())
#print(a.sum())
#print(a.sum(axis=0)) for colums
#print(a.sum(axis=1)) for rows within brackets
#print(np.sqrt(a))
#print(np.std(a))
#print(np.vstack((a,b)))
#print(np.hstack((a,b)))
#print(a.ravel()) single row
import matplotlib.pyplot as plt
#x=np.arange(0,3*np.pi,0.1)
##y=np.sin(x)
#y=np.tan(x)
#plt.plot(x,y)
#plt.show()
print(np.exp(a))
print(np.log(a))
print(np.log10(a))
















