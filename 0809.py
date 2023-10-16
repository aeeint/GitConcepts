# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:29:09 2023

@author: Teanie
"""
#exercice 1
i=0
average=0
while i<10:
    num=int(input("Enter an integer: "))
    average+=num
    i+=1
average=average/10
print(f"The average is {average}")

#exercice 2
num=int(input("Enter an integer:  "))
while num>0:
    res=num/3
    print(f"The division of {num} by 3 is {res}")
    num=int(input("Enter another integer"))
print("We're done!")

#exercice 3
num=int(input("Enter an integer: "))
count=0
while num>0:
    res=num/3
    count+=1
    print(f"The division of {num} by 3 is {res}")
    num=int(input("Enter an integer: "))
    
print(f"There are {count} operation")

#exercice 4
count=0
num=0
while num<=211:
    if num%3==0:
        count+=1
        
    num+=1
print(f"There is {count} numbers divisible by 3")

#exercice 5
sum=0
count=1
while count<=10:
    num=int(input("Enter an integer: "))
    sum=sum+num
    count+=1
print(f"The sum is {sum}")

#exercice 6
num=0
sum=0
while num<=10:
    sum=sum+num
    num+=1
print(f"the sum of the first 10 numbers is {sum}")

#exercice 7
i=1
while i<=4:
    print("*"*i)
    i+=1

#exercice 8    
num=int(input("Enter an integer: "))
num1=num
fact=1
while num>0:
    fact=fact*num
    num-=1
print(f"the factorial of {num1} is {fact}")

#exercice 9
name='Jesaa29Roy'
size=len(name)
i=0
while i<size:
    if name[i].isdecimal():
        break;
    print(name[i], end='')
    i+=1
print("\nThe execution has stopped")

#exercice 10
name='Jesaa29Roy'
size=len(name)
i=-1
while i<size-1:
    i+=1
    if not name[i].isalpha():
        continue;
    print(name[i], end='')
print("\nThe execution has stopped")

#exercice 11
n=int(input("Enter the value of n: "))
for i in range (n+1):
    q_i=i**2
    print(q_i)
    
