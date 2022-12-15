#files ore being taught in the the class
'''
import sys 
x=int(sys.argv[1])
y=int(sys.argv[2])
sum=x+y
print(sum)'''

'''fd=open("pes.txt","r")
line=fd.readline()
while(line):
    print(line)
    line=fd.readline()'''


# write a python program to print the following pattern
# abcd
# bcd
# cd
# d


'''s=input("enter the alphabets:")
def pattern():
    for i in range(len(s)):
        print(s[i:])
pattern()'''

# write a pyhton program to print the following pattern
#1
#12
#123
#1234

'''n=int(input("enter the numbers: "))

for i in range (1,n+1):
    for j in range (i):
        print(i , end=' ')
    print("\n")'''


#write program to find the frequency of words in a given string 
#ex:string="how much wood would a wood chuck chuck if a wood chuck could chuck wood"

'''s="how much wood would a wood chuck chuck if a wood chuck could chuck wood"

l=s.split()
print(l)
d={} #empty dictionary 

for i in l :
    if i not in d:
        d[i]=1   #add in dictionary
    else:
        d[i]+=1  #if presnt update 
print(d)'''


#write a program to create a set of all even numbers between 1 and 20 that are not divisible by 4 

'''s=set()
i=2
while (i<=20):
    if (i%4!=0):
        s.add(i)    
    i=i+2
print(s)'''
    
'''res=set(range(2,21,2))-set(range(4,21,4))
print(res)'''


#write programs for the following:  9 november
#1. List all the Unique States
#2. List of cities per state 
#3. count number of cities per state
#4. number of places for a city state combination (hint: use nested dictionary)

 # lines=s.split('\n')

 #working on Datasets
"""all ='''karnataka bangalore lalbagh
tamilnad Kanyakumari vivekananda_rock
kerala tiruvandapuram padmanabha_temple
karnataka Mysore brindavan_gardens
karnataka hassan shravanabelagola
tamilnad chennai egmore_museum
tamilnad kanyakumari kaamaakshmi_temple
karnataka bangalore cubbon_park
karnataka hampi maharnavami_dibba
karnataka bangalore ISKCON
karnataka hassan halebeedu
tamilnad chennai ashtalakshmi_temple
karnataka hampi purandara_mantapa
karnataka Mysore ambavilas_palace
kerala tiruvandapuram zoo
karnataka hassan belur
tamilnad chennai valluvar_kootam
karnataka hampi vijaya_vittal_temple'''


l=all.split("\n")

for i in l :
    print(i)
print(len(l))
state=set()
for i in all.split("\n"):
    #print(i.split()[0])
    state.add(i.split()[0])

print(state)"""


#write a program that output length of words in a string using user defined functions 

'''def fun():
    s="this is the end of unit2 today is 9november 2022"
    l=s.split()
    print(l)
    
    for i in l:
        print(i,"--",len(i))
fun()'''


#write a functions which prints even length words in a given sting 

'''def fun():
    s="this is the end of unit2 today is 9november 2022"
    l=s.split()
    print(l)
    
    for i in l:
        if len(i)%2==0:
            print(i,"--",len(i))
fun()'''


#given two strings , find common letters using functions

'''def commonletters(s1,s2):
    set1=set(s1)
    set2=set(s2)
    res=""
    for ch in set1 & set2:
        res+=ch
    return res

s1="cattle"
s2="concat"
print("common letters :",commonletters(s1,s2))
s3="horse"
print("common letters :",commonletters(s1,s3))
s4="zzzzz"
print("common letters :",commonletters(s3,s4))'''




