# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:35:30 2023

@author: Teanie
"""

import numpy as np
a=np.array([1, 2, 3], dtype='int32')
print(a.ndim)
# get the dimension, tab 1D, matrix 2D
print(a.shape)
#(nb of ligne, nb of elemnt in ligne)
print(a.dtype)
print(a.itemsize)
#return length in bytes
print(a.nbytes)
#total of bytes (x4)
print(a.size)
#get the number of element

b=np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(b[1, 5])
#get a specific element
print(b[0,:])
#get a specific row
print(b[:,2])
#get a specific column
print(b[0, 1:-1:2])
#[a, b:c:d] : a=row start, b=element in row, c=stop index (excluding), d=step size
#start at row a and end at row c exclued, start at b element in row and have a step size of d
print(b[:, 0:-1:2])
z=np.ones((2, 3))
print(z)
#declare matrix with only zeros or ones
np.full((2, 2), 99)
#like np.ones but with other value
c=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)
#mltiple matrix in a matrix
c[0, 1, 1]
#[a, b, c] : a=number of the matrxi, b=number of the row, c=number of column
np.full_like(a, 4)
#create a matrix with the same size and full of 4
np.random.rand(4, 2)
#create matrix with random value 
np.random.randint(-4, 8, size=(3, 3))
#create matrix with random value between 2 values
np.identity(5)
#create identity matrix
arr=np.array([[1, 2, 3]])
r1=np.repeat(arr, 3, axis=0)
print(r1)


#Exercice 1
ar=np.array([[1, 0, 1]])
r=np.repeat(ar, 3,axis=0)
r[1, 1]=2
print(r)


#Exercice 2
output=np.ones((5,5))
z=np.zeros((3, 3))
z[1, 1]=9
output[1:-1, 1:-1]=z
print(output)


#Exercice 3
d=np.random.rand(2, 3)
e=np.random.randint(-5, 5, size=(3, 2))
np.matmul(d, e)
#mltiply two matrix (can't multiply more than Two matrix)


#Exercice 4
f=np.random.randint(-10, 10, size=(4, 4))
g=np.random.randint(-4, 10, size=(3, 3))
print(np.linalg.det(f), np.linalg.det(g))


#Exercice 5
stats=np.array([[1, 2, 3], [4, 5, 6]])
print(stats)
print(np.min(stats))
print(np.max(stats))
print(np.min(stats, axis=0))
#axis=0 -->column
print(np.max(stats, axis=1))
#axis=1-->row
print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))


#Exercice 5
npoints=21
values=np.linspace(-2.0, 2.0, npoints)
#To get npoints between -2.0 and 2.0 equally spaced
print(values)


#Exercice 6
y=np.linspace(10, 30, 21)
x=np.arange(10, 30)
#y[4]=1
print(x)








