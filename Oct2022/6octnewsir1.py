#fibonacci series 
n=int(input("How many terms ?"))
n1,n2=0,1
count=0
if n<=0:
    print("Enter a positve integer")
elif n==1:
    print(n1)
else:
    print("Fibonacci Series is")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1