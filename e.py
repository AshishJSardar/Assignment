print("hello")

# Reverse the String
a="ashish"
b=a[::-1]
print(b)

# skip duplicate character
a='great responsibility'
b=' '.join(set(a))
print(b)

# skip duplicate character
a=['a','b','c','d','a','a','b','e','b']
b=list(dict.fromkeys(a))
print(b)

# remove duplicate 
dup=[1,2,3,4,5,6,2,3,4]
remove=list(dict.fromkeys(dup))
print(remove)

# Factorial
num=int(input("enter the number:"))
fact=1
for i in range(1, num+1):
    fact=fact*i
    print(fact)

# Odd / Even
num=int(input("enter the number:"))
if(num%2)==0:
    print("number is even")
else:
    print("number is odd")   

# reverse string
a="sardar"
b=reversed(a)
c=''.join(b)
print(c)

# reverse the order of string
a="ashish sardar"
b=a.split()
c=b[::-1]
d=''.join(c)
print(d)

# square root of no.
l1=[1,2,4,5]
for i in l1:
    print(i,i*i)

# one to one mapping
l1=[1,2,3]
l2=[4,5,6]
for i in l1:
    for j in l2:
        print(i,j)

# addition of number in two list
l1=[1,2,3] 
l2=[4,5,6]
l3=[l1[i]+l2[i] for i in range(len(l1))]
print(l3)

# merge the content of two list
l1=[1,2,3]
l2=[4,5,6]
l3=l1.append(l2)
print(l3)

# add one list in another list
l1=[1,2,3]
l2=[4,5,6]
l3=l1.extend(l2)
print(l3)

# multiplication of two matrices
import numpy as np
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[9,8,7],
   [6,5,4],
   [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

result=np.dot(a,b)
for r in result:
    print(r)

# merge two dict
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}

def merge(dict1,dict2):
    return(dict2.update(dict1))
print(merge(dict1,dict2))
print(dict2)  

# Fibbonacci Series
num=int(input("enter the number:"))
n1,n2=0,1
print("fibonacci series:",n1,n2,end="")
for i in range(2, num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end="") 
print()  

# Palindrome of no.
num=input("enter the no:")
if num==num[::-1]:
    print("the no is palindrome")
else:
    print("the no is not palindrome")

# Palindrome of string.
num=input("enter the string:")
if num==num[::-1]:
    print("the string is palindrome")
else:
    print("the string is not palindrome")

# sum programm
l1=[1,2,3,4,5,6]
sum=0
for i in l1:
    sum=sum+i
    print(sum)

# prime no
num=int(input("enter the no:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("no is not a prime")
            break
    else:
        print("no is prime")
else:
    print("no is not prime")