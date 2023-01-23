# def fun(num):
#     raise ZeroDivisionError  #explictily generating an error

# try:
#     fun(3)
# except ArithmeticError:      # parent class of zerodivisionerror
#     print("an error occured")
# except ZeroDivisionError:
#     print("guess the output")
# print("terminate")

# #CPU take the first match not the best match


# #example
# try:
#     x=int(input('Enter a number upto 100: '))
#     if x > 100:
#         raise ValueError(x)
# except ValueError:
#     print(x, "is out of allowed range")
# else:
#     print(x, "is within the allowed range")

# print("-------------------------------------------------")

# finally - basically use to release the resources aquired by the program 


class MyException(Exception):
	def __init__(self, str):
		self.str = str
	def __str__(self):
		return self.str
n = int(input("enter a number:"))
try:
    if not 1 <= n <= 100 :
        raise MyException("number not in range")
        print("number is fine : ", n)
except MyException as e:
        print(e)
print("thats all")


