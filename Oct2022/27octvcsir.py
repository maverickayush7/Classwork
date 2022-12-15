dict1={"abc":90,"def":67,"ghi":94}
sum1=0
for i in dict1.values():
    sum1+=i
avg =sum1 // len(dict1)
print(avg)