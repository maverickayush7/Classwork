import functools
l=[1,2,3,4]
res=functools.reduce(int.__add__,l)
print(res)


#---------------

cube=[]
for i in range (0,11):
    cube.append(i**3)
print("result =",cube)


cube=[x**3 for x in range (11)]
print("result =",cube)


l=[1,2,3,4]
res=[i**2 for i in l ]
print(res)




