# 1) program to find the maximum of a list of numerical values by using reduce()

import functools     
t=[1,2,3,4,5]
def maxi(x,y):
    if x>y:
        return x
    else:
        return y
y=functools.reduce(maxi,t)        # hint : to use reduce only change the import line 
print(y)


# 2) factorial using reduce ()
#* method 1
from functools import *

# def factorial(x,y):
#     return x*y

t=list(range(1,(int(input("enter the number :"))+1)))
# l=list(range(1,t+1))

# y=reduce(factorial,t)           # hint : to use reduce only change the import line 
y=reduce(lambda x,y:x*y , t)
print(y)

#* method 2
from functools import *
n=int(input("enter the number:"))
res=reduce(lambda x,y:x*y,range(1,n+1))
print(res)
