# 1) program to print odd numbers from the list using filter()

t=[1,2,3,4,5,6]
y=list(filter(lambda x:x%2 !=0 , t))
print(y)


# 2) program to find the difference between list using map()

l1=[1,2,3,4]
l2=[4,5,6,7]
y=list(map(lambda x,y : x-y ,l1,l2))
print(y)


# 3) program to remove stop words from string using filter()

l="this is the program to remove stop words from the given string"
y=l.split()
t=['is','the','to','from']
w=list(filter(lambda x: x not in t, y))
print(w)


# 4) program to extract the positive elements from the list using filter()  / define function also 

#*method 1
t=[12,-34,45,-25,67,-99]
y=list(filter(lambda x:x >0 ,t))
print(y)

#*method 2
def fpositive(x):
    if x>0:
        return x
res = list(filter(fpositive,t))
print(res)

#*method 3
def fpos(x):
    x=list(filter(lambda x:x >0 ,t))
    return x
print(fpos(t))


