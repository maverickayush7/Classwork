# program - define class called employee have 2 class varibles and 1 method 

class employee():
    company="maverick.ltd"
    address="Bengaluru"

    def display(this):
        print(this.company,this.address)
        
obj=employee()
obj.display()
print(employee.company)