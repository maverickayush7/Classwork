# polymorphism means when to apply and where to apply

# this is a dynamic ploymorphism
class A:
    def __init__(self):
        print("class A obj init")
    def m1(this):
        print("this is a method in class A")

# inheritance is used to extend the functionality

class B(A):
    def __init__(self):
        print("class B obj init")
    def m2(self):
        print("this is a method in class B")
    # def m1(self):
    #     print("this is a method in class B")

obj1=B()
obj1.m1()  #* over writes the parent method , first check sub class then goes to parent class 

# obj2=A()
# obj2.m2()  # base class can access parent class but parent class can't

#* inheritance is a relationship
#* composition has a relationship



print("---------------------------------------------------------")


# composition - has a relationship
class A:
    def __init__(self):
        print("class A obj init")
    def m1(this):
        print("this is a method in class A")

class B(A):
    def __init__(self):
        self.obj3=A()
        print("class B obj init")
    def m2(self):
        self.obj3.m1()
        print("this is a method in class B")
    # def m1(self):
    #     print("this is a method in class B")

obj1=B()
obj1.m2()
