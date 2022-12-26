# display a list of strings made of the first and last characters from a given list of words if the length of the string is greater than equal to 3

l=['CR7','Messi','Neymar','Lewandowski']
y=[i[0]+i[-1] for i in l if len(i)>=3]
print(y)


#count the no. of spaces in the string
l='This is final  exam'
y=len([i for i in l if i == ' '])
print(y)


#form a list of strings made of the first 2 and last 2 characters from a given list of words if the length of the string is greater than 4

l=['pear','apple','banana','kiwi']
y=[i[:2]+i[-2:] for i in l if len(i) >= 4 ] #slicing
print(y)


#find and display the intersection of to lists 

a=[1,2,3,4,5]
b=[4,5,6,7,8]
y=[i for i in a for j in b if i==j]  #logic 1
z=[i for i in a if i in b]           #logic 2  
x=list (set (a) & set (b))           #logic 3
w=set(a)        
print(y)
print(x)
print(w)
print(z)

