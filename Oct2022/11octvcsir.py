'''lst1=[1,2,3,4]
lst2=lst1
print(id(lst1))
print(id(lst2))'''

# add 100 to a list without any ulid in function
'''a = [10,20,30,40]
for i in range (len(a)):
    a[i]+=100
print(a)'''

#Pragram to find leftmost even number using while loop
'''found=False
a=[35,23,24,36,47,84]
i=0
while not found and (i<len(a)):
    if a[i]%2==0:
        found=True
    else:
        i+=1
if found:
    print("Found an even number :",a[i])'''

#arrange in descending order
'''a=[12,26,11,28,67]
a.sort(reverse=True)
print(a)'''

#12 october
'''c=[10,20,25,35,40,20]
res=[]
for i in range (len(c)-1):
    res.append(c[i+1]-c[i])
print(res)'''
'''p=[]
for i in range (3,32):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        p.append(i)
print(p)'''       

'''c=[1,1,3,5,6,7]
b=[1,4,6,3,8,10,3,6]
res=[]
for i in b:
    if i in c:
        res.append(i)
print(res)'''

#count the number of odd/even numbers , create there list , find the sum of odd and sum of even numbers
d=[1,2,3,5,22,31,121,66]
even=0
odd=0
e=[]
o=[]
se=0
so=0
for elem in d:
    if elem%2==0:
        even+=1
        se=se+elem
        e.append(elem)
    else:
        odd+=1
        so=so+elem
        o.append(elem)
print("No. of odd numbers :",even)
print("No. of odd numbers :",odd)

print(e)
print(o)
print("sum of odd numbers :",so)
print("sum of even numbers:",se)
