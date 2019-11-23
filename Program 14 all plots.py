# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:43:41 2019

@author: Kamran Hashmi
"""

import matplotlib.pyplot as plt
import matplotlib.style as st
'''x=([1,2,3],[6,5,4])
plt.plot([1,2,3],[4,5,1],label=1)
plt.plot([0,1,3],[7,4,1],label=2)
plt.plot([1,2,3],[3,5,2],label=3)
plt.legend()
plt.show()

x=[2,3,3]
y=[1,1,3]
plt.plot(x,y,label="label")
plt.legend()
plt.title("First")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
'''
#st.use("ggplot")#background color
'''X=[1,2,3]
Y=[4,6,5]

X1=[1,2,3]
Y1=[7,4,6]

x3=[2,2,2]
y3=[8,5,2]
x4=[2.5,2.5,2.5]
y4=[8,5,2]
plt.plot(x4,y4,'g',label="1",linewidth=2)
plt.plot(X,Y,'b',label="2",linewidth=3)
plt.plot(X1,Y1,'y',label="3",linewidth=5)
plt.plot(x3,y3,'k',label="4")
plt.legend()
plt.title("Let's see")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True,color='g')
plt.show()
x=[1,3,5,7,9]
y=[8,7,6,5,8]

X=[2,4,6,8,10]
Y=[4,3,2,1,4]
plt.plot(x,y,label="cyan",color='c',linewidth=1)
plt.bar(X,Y,label="green",color='g')
plt.legend()
plt.show()'''
#Histogram
'''
x=[9,9,9,22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
y=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(x,y,histtype="bar",rwidth=1,label="Histogram")
plt.title("Title")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()'''
#Scatter Plot
'''x=[5,2,3,4,1]
y=[5,4,3,6,7]
plt.scatter(x,y,label="Scitskat",color='c')
plt.legend()
plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

#Stack Plot
days=[0,1,2,3,4]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
plt.plot([],[],color='c',label="eating")
plt.plot([],[],color='m',label="Sleeping")
plt.plot([],[],color='r',label="Working")
plt.plot([],[],color='k',label="Playing")
plt.stackplot(days,eating,sleeping,working,playing,colors=['c','m','r','k',])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title('Stack Plot')
plt.legend()
plt.show()

'''