class Person: 
    def __init__(self,name,age): #constructor with arguments
        self.name = name
        self.age = age 
a = Person("Kavya",45) #class object 
b = Person("Amar",30) #class object 
print(a.name,a.age) 
print(b.name,b.age)
