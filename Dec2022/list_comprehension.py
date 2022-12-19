#list comprehension

l=["pesu","pesit","ayush"]
y=[l[i][(len(l[i])-1)] for i in range(0,len(l))]
print (y)


l1=[1,2,3,4]
l2=[5,6,7,8]
res=[(i,j) for i in l1 for j in l2 if i!=j]   # expression , nested for loop , if condition
print(res)


l1=[1,2,3,4]
l2=[5,2,8,3]
res=[i for i in l1 for j in l2 if i==j]   # expression , nested for loop , if condition
print(res)

l1=['pes',"pesit",'ayush']
res=[ (i, len(i)) for i in l1 ]
print(res)