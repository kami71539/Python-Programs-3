# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:08:39 2019

@author: Kamran Hashmi
"""

def mean(x):
    count=0
    s=0
    for i in x:
        count=count+1
        s=s+i
    mean=s/count
    return round(mean,1)

def median(x):
    x.sort()
    if len(x)%2==0:
        median=(x[len(x)//2]+x[len(x)//2-1])/2
        return median
    else:
        median=x[len(x)//2]
    return round(median,1)
def mode(x):
    count=0
    count_list=[]
    count_list_index=0
    x.sort() 
    for a in range(len(x)):
        b=x[a]
        for i in x:
            if b==i:
                count=count+1
        count_list.append(count)
        count=0
    for a in range(len(count_list)):
        if count_list[a-1]<count_list[a]:
            count_list_index=a
    mode=x[count_list_index]
    return mode
   
x=[64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]
print(mean(x))
print(median(x))
print(mode(x))
#----------------------
import statistics as stat
w=stat.mean(x)
y=stat.median(x)
def mode(x):
    try:
        z=stat.mode(x)
        return z
    except:
        x.sort()
        return(x[0])
z=mode(x)
print(f"{x} as list, {w} as median, {y} as median, and {z} as mode.",end=" ")
