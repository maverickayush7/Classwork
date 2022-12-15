#14/12/2022

'''res=list (map(len,["pes","pesit",'pesu']))
print(res)


res=list (map(lambda x:len(x)<5,["pes","pesit",'pesu']))
print(res)


res=list (filter(lambda x:len(x)<5,["pes","pesit",'pesu']))
print(res)


import functools
def sum(x,y):
    return x+y
re=functools.reduce(lambda x,y : sum(x,y) , [1,2,3,4,5,6])
print(re)


import functools
def sum(x,y):
    return x+y
re=functools.reduce(lambda x,y : sum(x,y) , [1,2,3,4,5,6])
print(re)'''


#Q) Take input as a list of string 
#l=['pes','pesu','pesit'] if the len of string is less the 4 then convert it to upper case 
l=["pes","pesit",'pesu']
res=list(map(str.upper,(filter(lambda x:len(x)<4,l))))
print(res)



from functools import *
l=[1,2,3,4]
res=reduce(lambda x,y : x*y,l)
print(res)


