# finally - basically use to release the resources aquired by the program 

try:
    fp=open("new.txt","w")  #if r then it will throw the error 
except FileNotFoundError:
    print("file not found")
finally:
    fp.close()    # better practice to do this 
    print("final statement")