try:
    print("hello")
    print(a)
except IndexError:
    print("index error")
except NameError:   #NameError is a class name (sub-class)
    print("name error")

# at line 3 "NameError" object is created and then it surf for the same object name in except


try:
    print("hello")
    # print(a)      # an object of type nameerror will be generated

except Exception:    # super-class  (first match)
    print("error")
except IndexError:
    print("index error")
except NameError:   #NameError is a class name (sub-class)
    print("name error")
else:
    print("no error")
