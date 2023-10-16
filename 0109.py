# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:36:55 2023

@author: Teanie
"""
#exercice 1
import math as m
num1=float(input("enter a numeric value: "))
num2=float(input("enter another numeric value: "))
sum=num1+num2
product=num1*num2
print("the sum of {} and {} is {} ".format(num1, num2, sum))
print("the product of {} and {} is {} ".format(num1, num2, product))

#exercice 2
T=float(input("enter a temperature: "))
K=T+ 273.15
print("{} C° in Kelvin is {} K". format(T, K))

#exercice 3
edge=float(input("enter the edge"))
area=edge*edge
volume=area*edge
print("the area of a cube of {} cm edge is {} cm2 and the volume is {} cm3".format(edge, area, volume))

#exercice 4
nb10=int(input("enter the number of 10 "))*10
nb20=int(input("enter the number of 20 "))*20
nb50=int(input("enter the number of 50 "))*50
sum=nb10+nb20+nb50
print ("it will be {} ".format(sum))

#exercice 5
radius=float(input("enter the radius of the circle"))
lenght=round(radius*2*m.pi, 2)
area=round(radius*radius*m.pi, 2)
print("the lenght of a circle with a radis of {} cm is {} cm and the area is {} cm2".format(radius, lenght, area))

#exercice 6
r=float(input("enter the radis of the sphere"))
A=4*m.pi*r**2
V=4*m.pi*r**3/3
print("a sphere of {} cm of radius have an aera of {} cm2 and a volume of {} cm3.".format(r, A, V))

#exercice 7
A=float(input("enter the value of A"))
Ea=float(input("enter the vale of Ea"))
T=float(input("enter the temperature in celcius"))+273.15
R=8.3144621
k=A*m.exp(-Ea/R*T)
print(k)

#exercice 8
from math import radians, cos
side1=float(input("enter the length of the first side "))
side2=float(input("enter the length of the second side "))
angle=float(input("enter the angle between them in degrees"))
angle=radians(angle)
side3=m.sqrt(side1**2+side2**2-2*side1*side2*cos(angle))
print(side3)