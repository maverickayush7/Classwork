class MyException(Exception):
	def __init__(self, str):  #constructor
		self.str = str
	def __str__(self):
		return self.str
n = int(input("enter a number:"))
try:
	if not 1 <= n <= 100 :
		raise MyException("number not in range")
	print("number is fine : ", n)
except MyException as e:
		print(e)     # error propagation
		print("thats all")

print("-------------------------------------------------------------")

class Myclass(Exception):
	def __init__(self, str):  #constructor
		self.str = str
	def __str__(self):
		return self.str

try:
	n = int(input("enter a number less than 100:"))
	if n > 100 :
		raise Myclass("number not in range")
except NameError:
	print("name error")
except Myclass as e:
		print(e)
