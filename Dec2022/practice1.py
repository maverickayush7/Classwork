# remove number divisible by 3 
l=[2,3,6,7]
y=[i for i in l if i%3 !=0]
print(y)

# display number of odd and palindrome from 20 to 100 
y=[i for i in range (20,101) if i%2!=0 and str(i)[0] == str(i)[-1]]
print(y)

 
#display maximum element in a given list 
y=[1,2,3,4,34,23]
s= [i for i in y if i==max(y)]
print(s)

#display list of number and list of strings .both the list of same size . combine two list to make a list of tuples
