'''import math
import random
print(dir(math))
r1=random.randint(0,10)
print(r1)
random.seed(6)
print(random.random())


num=int(input("Enter decimal value:"))
result=""
while num!=0:
    remainder=num%2
    num=num//2
    result=str(remainder)+result
print("The binary representation is",result)

for x in range(2,30,2):
   print(x)
list1=["abc","def","ghi"]
for i in list1:
   if i=="def":
      continue
print(i)

s=int('10A',16)
print(s)

e=9*16
print(e)

print(100//6%2-2**2**3)

for i in range(10,21,4):
   if i%5:
      print("Yes")

print("Face"'book')

print(chr(ord(chr(ord("a")+1))-1))

print(2>1<=9!=3)

x=10
y=50
if x**2 > 100 or y<100:
  print(x,y)'''

