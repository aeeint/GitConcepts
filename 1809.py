# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:25:13 2023

@author: Teanie
"""
#Exercise 1
num=input("Enter a value: ")
num_list=[]
sum=0
while num!="":
    num_list.append(num)
    num=float(num)
    sum=sum+num
    num=input("Enter a value: ")
average=sum/len(num_list)
print("The average is {}".format(round(average, 2)))


#Exercise 2
name=str(input("Enter the name of the people separated by blanks:\n "))
name_list=name.split()
for i in name_list:
    print("Hi "+i)
print("There is {} people".format(len(name_list)))


#Exercise 3
element=["H", "C", "N", "O", "S", "Cl"]
atomic_mass=[1.008, 12.011, 14.007, 15.999, 32.065, 35.453]
molecular_mass=0
for i in range(len(element)):
    compound=float(input("Enter the number of {}: ".format(element[i])))
    molecular_mass=molecular_mass+compound*atomic_mass[i]
print("The molecular mass is {:.3f}".format(molecular_mass))


#Exercise 4
n=int(input("Enter the degree n: "))
coef_list=[]
cnt=0
poly=0
for i in range(n+1):
    coef_list.append(int(input(f"Enter the coefficient (power {i}): ")))
x=float(input("Enter the value of x: "))
for element in coef_list:
    poly=poly+coef_list[cnt]*x**cnt
    cnt+=1
print(f"The result is {poly}")



























