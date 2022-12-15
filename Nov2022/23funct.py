'''def fun (x):
    print(x)
    x=20  #local
    print(x)

a=10  #global
fun(a)
print(a)



def fun(a):
    print(a)
    x=30

    def fun1():
        nonlocal x
        print(x) #30

        def fun2():
            print(x) #30

        fun2()
    
    fun1()
  
a=10  #global
fun(a)
print(a) #10






def fun(a):
    print(a) #10
    

    def fun1():
        
        print(a) #10

        def fun2():
            print(a) #10

        fun2()
    
    fun1()
  
a=10  #global
fun(a)
print(a) #10







def fun(x):
    x=[10,20]  #don't work

a=[1,2,3]
fun(a)
print(a) #[1,2,3]




def fun(x):
    x.append(20)  #works bcoz it is pass by reference 

a=[1,2,3]
fun(a)
print(a)  #[1,2,3,20]





def fun(x):
    x.append(20)  

a=[1,2,3]
fun(a)
print(a)  





def fun(x):
    print(x)
    print(id(x))
    x=20
    print(x)
    print(id(x)) 

a=10
print(id(a))
fun(a)
print(a)  
'''




'''def fun(x):
    x+=x

a=10
fun(a)
print(a)'''



def fun(x):
    print(id(x))
    x.append(40)
    x=[20,30]

    print(x)  #[20,30]



a=[1,2,3]
print(id(a))
a.append(30)

fun(a)
print(a)  #[1,2,3,30,40]







