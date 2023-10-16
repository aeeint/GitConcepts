# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:15:03 2023

@author: Teanie
"""
#FUNCTION
#def function_name(*args) : to put multiple arguments
#def function_name(**keyword) : to put multiple keyword (key = value)

#Exercice 1

def biggest(num1, num2):
    if num1> num2:
        print(f"{num1} is the biggest number")
    elif num1==num2:
        print(f"{num1} and {num2} are equal")
    else:
        print(f"{num2} is the biggest number")

num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
biggest(num1, num2)


#Exercice 2

def large_and_small(*number):
    number_list=[]
    for i in range(len(number)):
        number_list.append(number[i])
    max_num=max(number_list)
    min_num=min(number_list)
    print(f"The biggest number is {max_num} and the smallest is {min_num}")
    
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
num4=int(input("Enter the fourth number: "))
num5=int(input("Enter the fifth number: "))
large_and_small(num1, num2, num3, num4, num5)


#Exercice 3

try:
    num=int(input("Enter a number: "))

except ValueError:
    print("There is a value error")
else:
    if(num%2)==0:
        print("{0} is even".format(num))
    else:
        print("{0} is odd".format(num))
finally:
    print("Executed finally !")


#Exercice 4
while True:
    try:
        num=int(input("Enter a number: "))
        if(num%2)==0:
            print("{0} is even".format(num))
    
        else:
            print("{0} is odd".format(num))
        break#To stop the loop
    except ValueError:
        print("There is a value error")


#Exercice 5
while True:
    try:
        num=int(input("Enter a number: "))
        sum=0
        while num<0:
            num=int(input("Enter a positive number please: "))
        for i in range (1, int(num/2)+1):
            if num%i==0:
                sum+=i
        if sum!=1:
            print(f"{num} is not a prime number.")
        else:
            print(f"{num} is a prime number.")
        break
    except ValueError:
        print("There is a value error")






















