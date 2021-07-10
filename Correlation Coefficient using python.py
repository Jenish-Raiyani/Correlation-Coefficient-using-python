# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:27:50 2021

@author: J.K.Raiyani
"""
ls=[]
ls1=[]
n=int(input("Enter Total number of items :"))
for i in range(n):
    x=float(input("Enter X value : "))
    y=float(input("Enter y value :"))
    ls.append(x)
    ls1.append(y)
print("X = ",ls)
print("Y = ",ls1)
avgx=sum(ls)/n
avgy=sum(ls1)/n
print("Average of x is",round(avgx,3))
print("Average of Y is",round(avgy,3))
 
x1 = []
y1 = []
for i in range(len(ls) and len(ls1)):
    difference1 = ls[i] - avgx
    difference2= ls1[i] - avgy
    x1.append(round(difference1,3))
    y1.append(round(difference2,3))
print("(xi-x̅) = ",x1)
print("(yi-ȳ) =",y1)
 
squared_x1 = [num1 ** 2 for num1 in x1]
squared_y1 = [num2 ** 2 for num2 in y1]
print("squared_(xi-x̅)",squared_x1)
print("squared_(yi-ȳ)",squared_y1)

mult=[]
for j in range(len(x1) and len(y1)):
    difference1 = x1[j] * y1[j]
    mult.append(round(difference1,3))
print("(X - Mx)(Y - My) = ",mult)


sum_1=sum(squared_x1)
print("Sum of Squared_x1 :",sum_1)
sum_2=sum(squared_y1)
print("Sum of Squared_y1 :",sum_2)
sum_3=sum(mult)
print("Sum of (X - Mx)(Y - My) :",sum_3)

import math
multiplication=sum_1*sum_2
print("multiplication :",multiplication)
print("square root : ",math.sqrt(multiplication))

r=sum_3/math.sqrt(multiplication)
print("r =",round(r,3))
 