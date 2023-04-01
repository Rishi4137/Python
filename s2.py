import numpy as npy
import matplotlib.pyplot as plt
import datetime as dt

print("Enter the start,end and increment values or n")
n1=int(input())
n2=int(input())
inc=int(input())


def recf(n):
    if (n==0):
        return 0
    elif n==1:
        return 1
    else:
        return recf(n-1)+recf(n-2)

def plotcurve(x,y,curvelabel,xlabel,ylabel,title):
    plt.plot(x,y,label=curvelabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


x1= list(range(n1,n2+1,inc))
y1=[]

for i in x1:
    t1 = dt.datetime.now()
    z = recf(i)
    t2 = dt.datetime.now()
    tdif= t2-t1
    y1.append(tdif.total_seconds())

plotcurve(x1,y1,"Time for recf","n","time in seconds","performance measuerment of fib() function")
plt.legend()
plt.show()