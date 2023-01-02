'''# map
p=['ayush','new','year']
y=list(map(str.upper,p))         #str is the class descriptions
print(y)


# filter    -applied when the input & ouput are to be different

#1 only using filter
p=['ayush','new','year']
def fun(i):
    if len(i)>3:
        return i.upper()
t=list(filter (fun,p)) 
print(t)

e=list(filter(lambda i:fun(i),p))
print("hii",e)

#2 using both map & filter
p=['ayush','new','year']
y=list(map(str.upper,filter(lambda x: len(x) >3 , p)))
print(y)
'''


# reduce   -we have to import functools  * output will be only one element

import functools
t=[1,2,3,4,5]
y=functools.reduce(lambda x,y : x+y,t)
print(y)

#*working 
# bascially x will keep updating with the sum of initial 2 element

# Q) input and output

l1=[1,2,3,4]
l2=[4,5,6,7]
# output : [5,7,9,11]

y= list(map(lambda x,y:x+y,l1,l2))   # hint: we call more than one iterable objects 
print(y)
