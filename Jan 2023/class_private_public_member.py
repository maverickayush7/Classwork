class A:
    def __init__(self,name,age):
        self.__name=name
        self.age=age     #public member (can be accessed  inside & outside the class)
    def Print(self):
        print(self.__name)
        self.__age=40
        print(self.__age)
b=A("pes",50)
b.Print()

print(b.__name)




# class B(A):
#     def Print(this):
#         print(this.age)

# b=B()