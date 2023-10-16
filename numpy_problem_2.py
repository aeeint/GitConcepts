# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:37:02 2023

@author: Teanie
"""
import numpy as np
#1-Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
vect=np.arange(0, 21)
vect[(vect>=9) & (vect<=15)]*=-1
print(vect)

#2-Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
vect=np.arange(15, 56)
print(vect[1:len(vect)-1])

#3-Write a NumPy program to create a 3X4 array and iterate over it.
mat=np.random.randint(0, 10, (3, 4))
print(mat)
for i in range (3):
    for j in range(4):
        print(mat[i][j], end=" ")
#not sure about what we had to do

#4-Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
vect=np.random.randint(5, 50, (10))
print(vect)

#5-Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
vect=np.random.randint(0, 10, (5))
print(vect)

#6-Write a NumPy program to multiply the values of two given vectors.
vect1=np.random.randint(0, 10, (5))
vect2=np.random.randint(0, 10, (5))
print(vect1)
print(vect2)
for i in range (0,5):
    vect1[i]=vect1[i]*vect2[i]
print(vect1)
    
#7-Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
mat=np.random.randint(10, 21, (3, 4))
print(mat)

#8-Write a NumPy program to find the number of rows and columns in a given matrix.
mat=np.random.randint(10, 21, (3, 4))
print(mat)
dim=np.shape(mat)
print(f"There are {dim[0]} rows and {dim[1]} columns")

#9-Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
mat=np.zeros((4, 4))
mat[0::2, 1::2]=1#put 1 every two rows from the row n°0 and every twor columns from the columns n°1
mat[1::2, 0::2]=1
print(mat)

#10-Write a NumPy program to find common values between two arrays.
array1=[ 0, 10, 20, 40, 60]
array2=[10, 30, 40, 60]
array3=[]
for i in range (len(array2)):
    for j in range(len(array1)):
        if array2[i]==array1[j]:
            array3.append(array1[j])
print(array3)


#11-Write a NumPy program to get the unique elements of an array
arr=np.random.randint(0, 5, (10))
print(arr)
print(np.unique(arr))

#12-Write a NumPy program to compute the cross product of two given vectors.
arr1=np.random.randint(0, 5, (2, 2))
arr2=np.random.randint(0, 5, (2, 2))
print(arr1)
print(arr2)
print(np.cross(arr1, arr2))

#13-Write a NumPy program to convert cartesian coordinates to polar coordinates of a random 10x2 matrix representing cartesian coordinates.
mat=np.random.random((10, 2))
print(mat)
x=mat[:,0]
y=mat[:,1]
r=np.sqrt(x**2+y**2)
t=np.arctan2(y, x)
print(r)
print(t)

#14-Write a NumPy program to find the closest value (to a given scalar) in an array.
vect=np.arange(0, 100)
n=float(input("Enter a number: "))
print(np.intersect1d(vect, round(n)))













