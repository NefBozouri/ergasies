from calendar import c
import math
from ntpath import join
from re import X
message = input("Enter message: ")
l,li=[],[]
for i in (message):
    l.append(ord(i))
for i in l:
    li.append(int(bin(i)[2:]))
print (l,li)
A=[]
for i in li:
    x=int(str(i)[:2])
    y=int(str(i)[-2:])
    print (x,y)
    x1=str(x)
    y1=str(y)
    A.append(x1+y1)
print (A)
B=[]
for i in range (0,len(A)-4,4):
    B.append(int(A[i]+A[i+1]+A[i+2]+A[i+3]))
sum1=0
sum2=0
sum3=0
sum4=0
p1=0
p2=0
p3=0
p4=0
def my_function(p,summ,i):
    p=p+1
    summ=summ+i
    return p,summ

for i in B:
    if i%2==0:
        my_function(p1,sum1,i)
    if i%3==0:
        my_function(p2,sum2,i)
    if i%5==0:
        my_function(p3,sum3,i)
    if i%7==0:
        my_function(p4,sum4,i)
if p1!=0:
    print ("Pososto zygwn:",(sum1/p1)*100)
if p2!=0:
    print ("Pososto pou diaireitai me to 3:",(sum2/p2)*100)
if p3!=0:
    print ("Pososto pou diaireitai me to 5:",(sum3/p3)*100)
if p4!=0:
    print ("Pososto pou diaireitai me to 7:",(sum4/p4)*100)







