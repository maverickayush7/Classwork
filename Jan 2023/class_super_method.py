class A:
    def __init__(this):
        this.abc=100  #public member
    def Print(this):
        print(this.abc)

class B(A):
    def __init__(this):
        super().__init__()  #invoke
        this.xyz=222
        print(this.xyz)
obj1=B()
obj1.Print()