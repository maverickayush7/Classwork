'''def triangle():
    print("tri")

def square():
    print("squ")

def rectangle():
    print("rec")

def draw(shape):
    shape()

draw(triangle)
draw(square)
draw(rectangle)'''


def f1(*a):
    x=(a[0]+a[1]+a[2])/(a[0]-a[1]-a[2])
    print(x)

def f2(*b):
    res=(b[0]*b[0])/(b[1]*b[1])+(b[2]**2)-(b[3]**2)
    print(res)

def outer(function,*arg):
    function(*arg)

outer(f2,4,2,3,5)
outer(f1,12,2,4)