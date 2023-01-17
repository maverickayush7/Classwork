# program - define class called employee have 2 class varibles and 1 method 

class employee():
    company="maverick.ltd"
    address="Bengaluru"

    def display(this):
        print(this.company,this.address)
        
obj=employee()
obj.display()
print(employee.company)


# 2) inherited class 

class animal:         # base class
    no_legs=4
    def sound(abc):
        print("universal sound")
    def display(this):
        print(this.no_legs)
class dog(animal):     # sub class   # used for extending the functionality
    colour="white"
    def sound(self):
        print("bow bow")

obj1=animal()
obj2=dog()
obj1.sound()
obj2.sound()
obj2.display()
obj1.display()