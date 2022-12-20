#dsiplay string following the given conditions
l=['pesse','ayush','helloworl']
y= [i for i in l if len(i)>5 and len(i)<10]
print(y)


# display thenumber if it is divisible by both 2 & 3 
l=[15,30,18,14]

y=[i for i in l if i % 2 == 0 and i % 3 == 0 ]  # [i for i in l if i % 2 == 0 if i % 3 == 0 ]

print(y)


# displays (even odd even odd ...) as a output
l=[1,3,4,6,8,2,7]

y=["EVEN" if i % 2 == 0 else "ODD" for i in l]

print(y)

# without list comprehension
l2=[]
for i in l:
    if i%2==0:
        l2.append("even")
    else:
        l2.append("odd")

print(l2)