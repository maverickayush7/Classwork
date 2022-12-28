l=[1,2,3,4]
'''for i in l:
    print(i)
'''

#step 1: create an iterator object call a function called iter()
#step 2: call function called next()

l=[1,2,3,4]
obj=iter(l)
'''print(type(obj))
print(next(obj))  #initialized to 1 
print(next(obj))  #2 
print(next(obj))  #3
print(next(obj))  #4
print(next(obj))  # 'stop iteration' is a run time error '''


l=[1,2,3,4]
obj=iter(l)
for i in obj:  # iterator object is also iterable 
    print(i)

