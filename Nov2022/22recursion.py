'''def fact(n):
    if n==0:
        return 1
    else:
        return(n*fact(n-1))

print(fact(3))'''



'''def fibo(n):
    a,b=0,1
    while a<n:
        print(a,end='')
        a,b=b,a+b
        print() 

fibo(100)
'''

#fibonacci series using recursion 

'''n=int(input("enter the number :"))

def fib(n):
    if n<=1:
        return n 
    else:
        return (fib(n-1)+fib(n-2))

for i in range(n):

    print(fib(i))'''


#write a python using recursion to find the GCD(greatest common diviser) of two number 

a=int(input("Enter the number :"))
b=int(input("Enter the number :"))

def gcd(a,b):
    if a==b:
        return a
    elif a<b:
        return gcd(b,a)
    else:
        return gcd(b,a-b)

print(gcd(a,b))


'''def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd(b,a-b)
    else:
        return gcd(b,a)'''
