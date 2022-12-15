'''l=[]
for i in range(1,6):
    l.append(i)
    print(l)

for i in range(1,6):
    for j in range (1,i+1):
        print(j,end=' ')
    print()

n=int(input("enter the list size "))
inp=[]
for i in range (n):
    inp.append(int(input("enter the emlements")))
print(inp)

print(print(print(end = ""),end = ""))

#Reverse number 

n = int(input("Enter a number: "))  

rev = 0  

while n!=0:
    r = n%10
    rev = rev * 10 + r
    n = n//10  

print("Reversed number:",rev)

#deciaml number to binary number 

number = int(input("Enter a decimal number \n"))  

result=""  

while number != 0:  

    remainder = number % 2 # gives the exact remainder  

    number = number // 2  

    result = str(remainder) + result  

print("The binary representation is", result)

#Calculate the lcm of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    greater = num1
else:
    greater = num2
while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1
print("LCM of",num1,"and",num2,"=",greater) 

num1=int (input("enter first number:"))
num2=int (input("enter second number:"))
se=0
so=0
if num1>num2:
    while(num2<=num1):
        if num2%2==0:
            se= se+num2
            num2=num2+1
        else:
            so=so+num2
            num2=num2+1
else:
     while(num1<=num2):
        if num1%2==0:
            se= se+num1
            num1=num1+1
        else:
            so=so+num1
            num1=num1+1
print("sum of even numbers:",se)
print("sum of odd numbers:",so)'''

for i in range (59):
    pass
print(i)