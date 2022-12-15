#12/12/2022 
'''#think before you ink 

#1 length of individual list 
#input : l=['abc','def','1234']
#output : l1=[3,3,4]

l=['abc','def','1234']
def fun(y):
    result=[]
    for i in y :
        result.append(len(i))
    return result

result=fun(l)
print(result)


#2 upper case
#input : l=['abc','defg','xyz']
#output : l1=['ABC','DEFG','XYZ']

l=['abc','def','1234']
def fun(y):
    result=[]
    for i in y :
        result.append(str.upper(i))
    return result

result=fun(l)
print(result)



#3 square 
#L=[1,2,3,4]
#L1=[1,4,9,16]

l=[1,2,3,4]
def fun(y):
    result=[]
    for i in y :
        result.append(i*i)
    return result

result=fun(l)
print(result)



l=[1,2,3,4]
def fun(y):
    l2=[]
    for i in y:
        l2.append(i*i)
    return l2

l2=fun(l)
print(l2)'''


b=["abc","pes","pesu","pessit"]
res=list(map(len,b))
print(res)

#type casting to be studied

b=["abc","pes","pesu","pessit"]
res=list(map(str.upper,b))
print(res)


b=[11,22,33,44]
res=list(map(lambda x:x*x,b))
print(res)


#maps function 
# program to display table of any value enter till n

n=int(input("Enter the number:"))
def table(n):
    for i in range(1,11):
        print(n ,"x", i , "=" , n*i ) 
print(table(n))


#using map 
i=int(input("enter the number :"))
def foo(i):
    prod = n*i
    return str(n)+ "x" +str(i) + "=" + str(prod)+"\n"
for line in map(foo,range (1,11)):
    print(line,end=" ")