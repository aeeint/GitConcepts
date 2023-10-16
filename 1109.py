# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:17:05 2023

@author: Teanie
"""

#exercice 1
n= int(input("Enter an integer: "))
for i in range (1, n+1, 2):#(a, b, c)-->a=starting point, b=ending point, c=step size
    q_i=i**2
    print(q_i)
    
#exercice 2
sum=0
for i in range(6):#n iterations from 0, here from 0 to 5
    sum+=i
    print(f"The value of sum is in each interation: {sum}")
print(f"The sum is valid {sum}")

#exercice 3
n= int(input("Enter an integer: "))
prod=1
for i in range(1, 6):#starting point: 1, ending point (not included): 6, step size 1
    prod=prod*n
    print(f"The value of product is in each interation: {prod}")
print(f"The product is valid {prod}")

#exercice 4
for i in range(4):
    for j in range(3):
        print("i= {}, j= {}".format(i, j))

#exercice 5
n=int(input("Enter the value of n (positive): "))
while n<0:
    n=int(input("Enter a positive value of n: "))
sum=0
for i in range(1, n+1):
    sum+=i
    print(f"The value of sum is in each interation: {sum}")
print(f"The sum is valid {sum}")

#exercice 5
n=int(input("Enter the value of n: "))
sum=0
for i in range (1, n+1):
    sum+=(i+1)/i**2
    #print("The value of sum is in each interation: {}".format(round(sum, 2)))
    print(f"For n= {n} the sm is {sum: .2f}")
print("The sum is valid {}".format(round(sum, 2)))

#exercice 6
n=int(input("Enter the value of n: "))
while n<0:
    n=int(input("Enter a positive value of n: "))
fact=1
for i in range(1, n+1):
    fact*=i
print(f"The factorarial of n={n} is {fact}")

#exercice 7
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}{j}")
        
#exercice 8
for i in range(1, 10):
    for j in range(1, 10):
        if i!=j:
            print(f"{i}{j}")

#exercice 9
n=int(input("Enter the number of line: "))
for i in range (1, n+1):
    T=i*(i+1)/2
    print(f"With {i} lines there are {T} points")
    
#exercice 10
for i in range(0, 10):
    for j in range (0, 10):
        for k in range (0, 10):
            print(f"{i}{j}{k}", end=", ")
            
#exercice 11
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i+j+k==22:
                print(f"{i}{j}{k}", end=' ')
                
#exercice 12
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i**3+j**3+k**3==i*100+j*10+k:
                print(f"{i}{j}{k}", end=" ")

#exercice 13
n=int(input("Enter a positive integer: "))
count=0
for i in range (1, n+1):
    if n%i==0:
        q=n%i
        count+=1
        print(f"{n} is divisible by {i}")
print(f"{n} have {count} positive divisors")

#exercice 14
n=int(input("Enter an integer: "))
sum=0
for i in range(0, n):
    odd=2*i+1
    sum+=odd
    print(f"{odd}", end=" ")
print(f"\nThe sum of the {n} first odd numbers is {sum}")

#exercice 15
n=int(input("Enter an integer (>1): "))
sum=0
for i in range (1, int(n/2)+1):
    if n%i==0:
        sum+=i
if sum!=1:
    print(f"{n} is not a prime number.")
else:
    print(f"{n} is a prime number.")
ans=str(input("Do you want to test another integer? (y/n): "))
while ans=='y':
    n=int(input("Enter an integer: "))
    sum=0
    for i in range (1, int(n/2)+1):
        if n%i==0:
            sum+=i
    if sum!=1:
        print(f"{n} is not a prime number.")
    else :
        print(f"{n} is a prime number.")
    ans=str(input("Do you want to test another integer? (y/n): "))
    
#exercice 16
num1=0
num2=1
n=int(input("Enter the vale of n: "))
for i in range(0, n):
    fibo=num1+num2
    num1=num2
    num2=fibo
print(num2)
















