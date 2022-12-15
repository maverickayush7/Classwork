'''def unique_list(l):
    x =[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,3,3,3,4,5]))

'''

'''a=['karnataka','tamilnadu','karnataka','karnataka','tamilnadu','kerala']
b=['mysore','chennai','hassan','shimoga','madurai','trivandrum']

def dictionary_fun(a,b):
    d={}
    for i in range(len(a)) :
        k=a[i]
        if k not in d:
            d[k]=[]
        d[k].append(b[i])
    print(d)
dictionary_fun(a,b)

'''

#reverse a string usoing recursion

def rev(s):
    if s=='':
        return ''
    else:
        return s[-1] + rev(s[:-1])
string=input("Enter a string :")
print('Reverse of--',string,'--is--',rev(string))
