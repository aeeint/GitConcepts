# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:16:45 2023

@author: Teanie
"""
#Fonctions
message='hello world'
print(len(message))
#donne la longueur du mot

print(message[3])
#donne le 3ème charactère du mot (premier: i=0)

print(message[0:3])
#donne une partie de la chaine de charactère

print(message[:5])
#donne une partie de la chaine de charactère du premier au iéme

print(message[: -1])
#donne toute la chaine de charactère sauf le dernier charactère

print(message.find(('o')))
#donne l'indice du charactère demandé

print(message.count('l'))
#donne le nombre d'occurence d'un charactère

print(message.lower())
#met en minuscule

print(message.upper())
#met en majscle

new_message=message.replace('world',' Irlande')
print(new_message)
#remplace une partie de la chaine de charactère

print(dir(str))
#pour connaitre toute les fonctions que l'on peut appliquer à un string

#exercice 1
num=input("ENTER AN INTEGER: ")
num=int(num)
if num<5:
    print("It's less than 5") 
else:
    print("It's greater than or equal to 5")

#exercice 2
num1=int(input("Enter an integer: "))
if num1%2==0:
    print("The number {} is an even number".format(num1))
else:
    print(f"The number {num1} is an odd number")

marks=float(input('enter your marks: '))
if marks<40:
    print("The student has failed and got an F grade")
elif marks>=40 and marks<=50:
    print("The student has passed marginaly and got an E grade")
elif marks>=50 and marks<=75:
    print("The student has passed with C grade")
elif marks>=75 and marks <=90:
    print("The stdent has done well and has scored B grade")
else:
    print("The student has done excellent and passed with distinction, A grade")
#elif --> else if

#exercice 3
weight=float(input("Enter yor weigth in kg: "))
height=(input("Enter your height in m or cm: "))
BMI=round(weight/height**2, 2)
print(BMI)
if BMI<18.5:
    print("you're underweight")
elif BMI>=18.5 and BMI<25:
    print("you have a normal weight")
elif BMI>=25 and BMI<30:
    print("you're overweight")
else:
    print ("you have obesity")

#exercice 4    
n1=int(input("Enter a first integer: "))
n2=int(input("Enter a second integer: "))
result1=n1//n2
result2=n1%n2
if result2==0:
    print(f"{n1} is divisible by{n2} and the result is {result1}")
else:
    print(f"{n1} is not divisible by {n2} and the result is {result1} and the rest is {result2}")

#exercice 5     
number1=float(input("enter a first integer: "))
number2=float(input("enter a second integer: "))
if number1<number2:
    print(f"{number1} is the minimum")
elif number1>number2:
    print(f"{number2} is the minimum")
else:
     print("They are the same integer so they both are the minimum") 
print("the minimum is {}".format(min(number1, number2)))
#min->trouve le minimum
 
#exercice 6      
unit=int(input("Enter the number of unit: "))
if unit<=100:
    print("no charge")
elif unit<200:
    unit=(unit-100)*5
    print(unit)
elif unit>=200:
    unit=(unit-200)*10+100*5
    print(unit)

