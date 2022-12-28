'''Generators: is used to create iterators using functions ''' 

'''def func():
    for i in range(5):
        return i**2 

print(func())'''


def func():
    for i in range (5):
        yield i**2       # we can store the previous value and move to next value

obj=func()
print(type(obj))   # class <'generator'>
print(next(obj))   #0
print(next(obj))   #1
print(next(obj))   #2
print(next(obj))   #3
print(next(obj))   #4
print(next(obj))   #'stop iteration'  can be handled by "exception handling" 
