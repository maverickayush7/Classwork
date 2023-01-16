class Dog:
    attr="mammal"    #class variable
    def bark(self):   #method
        a=20     #instance variable (values might be same but copies are different)
        print("barking")
        print(a)

obj1=Dog()  # constructor called as soon as object is created
obj2=Dog() 
obj3=Dog() 
obj1.bark()
obj2.bark()

print("---------------------------------------------")


class Dog:
    attr="mammal"    #class variable
    def bark(self,num):   #method
        a=num     #instance variable (values might be same but copies are different)
        print("barking")
        print(a)

obj1=Dog()    # constructor called as soon as object is created
obj2=Dog() 
obj3=Dog() 
obj1.bark(20)
obj2.bark(30)
print(Dog.attr)  #class attribute can be accessed outside
print(obj1.attr)
print("------------------------------------------------")




# create a class fruit ,have a method , one feature and 2 objects 

class Fruit:
    catg="eatable"
    def eat(self):
        print("eating")

mango=Fruit()
mango.eat()



class Fruit:              #parametrised constructor
    catg="eatable"
    def __init__(self,name):
        fruit=name
        print(fruit)
    def eat(self):
        print("eating")

obj1=Fruit("mango")
obj2=Fruit("orange")

obj1.eat()



