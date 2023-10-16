# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:05:32 2023

@author: Teanie
"""

import numpy as np

#Create a vector from multiple input
#First method: 
nel=int(input("Enter the number of elements in the vector: "))
lvec=[]
for i in range(nel):
    comp = input("Enter the value of component {} ".format(i))
    lvec.append(float(comp))
vec = np.array(lvec)#To create a vector from a list
print(vec)
#2nd method: 
nel=int(input("Enter the number of elements in the vector: "))
vec=np.zeros(nel)
for i in range(nel):
    comp = input("Enter the value of component {} ".format(i))
    vec[i]=float(comp)
print(vec)
#3d method: 
lin=input("Enter the components of a vector in a line: ")
smooth=lin.split()
vec=np.float_(smooth)#To put all values as float from a list
print("List: {} ".format(smooth))
print("Vector: {} ".format(vec))


#Create a matrix from multiple input
#First method: 
mat=np.zeros((4,3))
for i in range(4):
    for j in range(3):
        mat[i,j]=float(input("Introduce the value of the element ({}, {}): ".format(i,j)))
print(mat)


#Exercise 1
d=int(input("Enter the dimension: "))
A=np.zeros((d,d))
B=np.zeros((d,d))
for i in range (d):
    for j in range(d):
        A[i,j]=float(input("Enter the value of the element ({}, {}) for the matrix A: ".format(i, j)))
        B[i,j]=float(input("Enter the value of the element ({}, {}) for the matrix B: ".format(i, j)))
print(A)
print(B)
C=np.matmul(A, B)
print(C)
D=np.linalg.inv(C)
print(D)
A1=np.linalg.inv(A)
B1=np.linalg.inv(B)
print(np.matmul(A1, B1))
if np.allclose(D, np.matmul(A1, B1)):#np.allclose to compare 2 matrix
    print("its equal")
else:
    print("its not equal")



#Exercise 2
A=[[1, 1], [1, 2]]
B=[[4, 1], [3, 1]]
C=[[24, 7], [31, 9]]
A1=np.linalg.inv(A)
B1=np.linalg.inv(B)
X=np.linalg.inv(A)@C@np.linalg.inv(B)
print(X)
print(A@X@B)#@ to multiply 2 or more matrix


#Exercise 3
import math as m
list1=[2.07E-5, 2.62E-7, 3.22E-5, 2.59E-4, 4.87E-5, 1.19E-4, 3.95E-5]
vec=np.array(list)
list2=[]
for element in list:
    list2.append(round(-1*m.log10(element), 8))
print (list2)




"""Hello sir, I already sent you my exercice on monday of the reeding week by mail but I forgot to
write comments so I also submit it on Moodle but this time with comments.
Good afternoon, 
Teanie Kim MIOSOTIS 73174 """



#Convert Angstroms to Nanometers
vec=np.linspace(1.0, 5.0, 21)#create a vector of angstroms values between 1 and 5 with 21 values equally seperated
vector=np.linspace(vec[0]*10**-9, vec[len(vec)-1]*10**-9, 21)#create a vector of nanometers vectors from converted angstroms
print("Å: ", vec, '\nnm:', vector)



#Table of values
def function(x, x0, s):#create a function which calculate f(x)
    res=round((1/m.sqrt(2*m.pi))*m.exp((-1/2)*((x-x0)**2)/s**2), 5)
    return res
    
x0=float(input("Enter the value of x0: "))#ask values to the user
s=float(input("Enter the value of s: "))
x_in=float(input("Enter the value of the initial x: "))
x_fi=float(input("Enter the value of the final x: "))
n=int(input("How many x would you like to try ?: "))
X=np.linspace(x_in, x_fi, n)#create a vector with values entered by the user
Y=[]#create an empty list
for element in X:
    Y.append(function(element, x0, s))#add the values calculated by the function
for i in range(len(X)):
    print(round(X[i], 3), "  ", Y[i])#round the values and print the result



#Sea temperature statistics
import statistics as stat
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
temp=np.array(temp_mar)#Convert list temp_mar in vector temp
print(f"The average sea surface temperature in 2014 is {round(stat.mean(temp), 1)}°C")
ind_min=temp_mar.index(min(temp))#get the index of the minimum temperature
print(f"{months[ind_min]} has the coldest sea surface and its temperature is {min(temp)}°C")
ind_max=temp_mar.index(max(temp))#get the index of the maximum temperature
print(f"{months[ind_max]} has the warmest sea surface and its temperature is {max(temp)}°C")



#Exam grades
nb_stud=int(input("Enter the number of students who took the exam: "))
student=np.arange(0.0, nb_stud)#create vector of students number with only zeros
theory=np.zeros(nb_stud)#create vector of theory grades with only zeros
problem=np.zeros(nb_stud)#create vector of problem grades with only zeros
total=np.zeros(nb_stud)#create vector of total grades with only zeros
for i in range(nb_stud):#for loop to the values entered by the user in the vectors for each student
    theory[i]=float(input(f"Enter the mark of student n° {i} for the theory part between 0 and 10 : "))
    problem[i]=float(input(f"Enter the mark of student n° {i} for the problem part between 0 and 10 : "))
    total[i]=theory[i]*0.4+problem[i]*0.6#calculate the average of each student
print(f"The maximum mark is {max(total)}, the minimum mark is {min(total)}, and the average is {stat.mean(total)}")
print(student, '\n',theory, '\n', problem, '\n', total)
index, =np.where(total==max(total))#get the index of the maximm grades
print(f"The student with the highest mark is student n°{index}!")



























