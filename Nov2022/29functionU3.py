'''def outer(msg):
    print("outer")

    def inner(): #inner function
        print(msg)
    
    return inner


fun=outer("pesu:this is the example of closure")  #outer function
print(type(fun))
fun()'''


'''def outer(msg):
    print("outer")

    def inner(): #inner function
        print(msg)
    print("inner id:",id(inner))
    return inner

del outer # will not affect the code 
fun=outer("pesu:this is the example of closure")  #outer function
print(type(fun))
print("fun id:",id(fun))

fun()'''


"""i=int(input("enter:"))
def f1():
    print("outer")#outer function
    def f2(): #inner function
        print ("Hello")
        print ("world")
    print('f2=',id(f2))

    if (i==0):
        return f2
    else:
        del f2

c=f1()
c()
'''c()#refers to f2() if value of i is 0 otherwise it leads to error as f2() gets deleted
i=int(input())
f1()# creates a new instance of f2()
c()#refers to older instance of f2()
print('c=',id(c))#id of c will be same as id of older instance of f2()
'''
"""

'''
def outer(x):
    result=0

    def inner(n):
        nonlocal result

        while (n>0):
            result=result+x*n
            n=n-1

        return result

    return inner

f1=outer(7)
print(f1(3))'''

def print_msg(msg):
    a=20

    def printer():
        print("a=",a)
        print(msg)
    return printer

another=print_msg("hello")

del print_msg

another()
