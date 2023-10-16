# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:11:30 2023

@author: Teanie
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2, 2, 101)
y=x**2
plt.xlabel("x")
plt.ylabel('f(x)')
plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 2.5)

plt.plot(x, y)#vectorsx, y
plt.title('Chart title')
plt.show()

x=np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')


x=np.linspace(-2, 2, 101)
y=x**2
plt.xlabel("x")
plt.ylabel('f(x)')
plt.plot(x, y,'g',  label="x**2")
plt.savefig("fig1.png")
y2=x**4
plt.plot(x, y2,'b',  label="x**4")
plt.savefig("fig2.png")
y3=x**3
plt.plot(x, y3, 'ro', label='x**3')
plt.savefig("fig3.png")
plt.legend()
plt.show()


#S10_1 Trigonometric function
nb=int(input("Enter the number of point to draws: "))
x=np.linspace(-1, 1, nb)
plt.xlim(-1, 1)
y=np.cos(2*np.pi*x)
plt.plot(x, y, label='cos(2pix)')
plt.title('Body function (2pix)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('cos2pix.png')
plt.show()


#S10_2
nb=int(input("Enter the number of point to draws: "))
x=np.linspace(-1, 1, nb)
plt.xlim(-1, 1)
y=np.cos(2*np.pi*x)
plt.plot(x, y,'r', label='cos(2pix)')
plt.title('Body function (2pix)')
y2=np.sin(2*np.pi*x)
plt.plot(x, y2,'b', label='sin(2pix)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("trigonometric", format="png")
plt.legend()
plt.show()


#S10_3 Importance of the nmber of points in the representation
while True:
    try:
        n=int(input("Enter the number of point to draws: "))
        while n<0:
            print("There is a value error? please enter a positive value")
            n=int(input("Enter the number of point to draws: "))  
        x=np.linspace(0, 4, n)
        y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
        plt.plot(x, y,)
        plt.show()
        break
    except ValueError:
        print("There is a value error")


#S10_4 ISOTHERM OF AN IDEAL GAS
num=int(input("Enter the number of point to draws: "))
T=int(input("Enter the temperature of the gas: "))
x=np.linspace(2, 10, num)
y=0.08206*T/x
plt.plot(x, y)
plt.title('Isotherm (idel gas)')
plt.xlabel('Vm (L)')
plt.ylabel('P (Pa)')
plt.savefig('isotherm.png')
plt.show()


#S10_5 COMPARAISON OF ISOTHERM OF AN IDEAL GAS
num=int(input("Enter the number of point to draws: "))
nb_temp=int(input("Enter the number of temperature you want to try: "))
x=np.linspace(2, 10, num)
for i in range (1, nb_temp+1):
    T=int(input("Enter the temperature of the gas: "))
    y=0.08206*T/x
    plt.plot(x, y)
plt.title('Isotherm (idel gas)')
plt.xlabel('Vm (L)')
plt.ylabel('P (Pa)')
plt.savefig('isotherm.jpg')
plt.show()


#S10_6 Gaussian function
x0=float(input("Enter the value of x0: "))
s=float(input("Enter the value of s: "))
x_in=float(input("Enter the value of the initial x: "))
x_fi=float(input("Enter the value of the final x: "))
num=int(input("Enter the number of point to draws: "))
X=np.linspace(x_in, x_fi, num)
y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((X-x0)**2)/s**2)
plt.plot(x, y)
plt.title('Gaussian function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('gauss.jpg')
plt.show()


#S10_7 Comparision of different function
num=int(input("Enter the number of point to draws: "))
x=np.linspace(0, 3, num)
y=np.exp(-x)
plt.plot(x, y, label='e(-x)')
y2=np.sin(3*np.pi*x)*y
plt.plot(x, y2,label='sin(3pix)e(-x)')
plt.title('Comparision of functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('comparision.jpg')
plt.legend()
plt.show()



#S10_8 Comparision of Gaussian function
num=int(input("Enter the number of point to draws: "))
num_func=int(input("Enter the number of functions to draws: "))
x_in=float(input("Enter the value of the initial x: "))
x_fi=float(input("Enter the value of the final x: "))
for i in range(num_func):
    x0=float(input("Enter the value of x0: "))
    s=float(input("Enter the value of s: "))
    X=np.linspace(x_in, x_fi, num)
    y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((X-x0)**2)/s**2)
    plt.plot(x, y, label='x0='+str(x0)+', '+'s='+str(s))
plt.title('Gaussian function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('gaussianes.png')
plt.legend()
plt.show()


























