# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:24:16 2023

@author: Teanie
"""

#Lists
fam=['Teanie', 'Nicolas', 'Tara', 'Cléa', "Mathias","hiba", "Maman"]
#declare a list
lista=range(5)
#to create a list with integer from 0 to 5 (excluded)
#a string is also a list, it's a list of character
#a list can have multiple type of data
print(fam[1])
#To access a certain element of the list
for name in fam:
    print(name)
#print all the elements in the list
print(fam[1::3])
#list[n::i] take the n element and skip i-1 elements, here starts with the element 1 and skip the element 2 and 3
print(fam[5][1])
#When list in list, writing index 1 from the list in random[5]
print(fam.pop(3))
#remove an element an save it

#Lists are mutables:
fam.append('Papa')
#To add an elemnt
fam.remove('hiba')
#to remove an element
fam[5]='bye bye'
#to change an element


#Tuples
family=('Maman', 'Papa', 'Teanie', 'Matteo', 'Timothy', 'Choco', 'Lily', 'Léo', 'Glagla')
#same as a list but tuples aren't mutables (add, remove or change)


#Sets
cats={'choco','Léo', 'Glagla', 'Lily'}
#same as list but can't have duplicats

#Exercice 1
a=['Teanie', 'Nicolas', 'Tara', 'Cléa', "Mathias","hiba", "Maman"]
print(a[1])
a.append('Papa')
print(a)
a.remove('hiba')
print(a)
a[4]='bye bye'
print(a)

#Exercice 2
family=['Maman', 'Papa', 'Teanie', 'Matteo', 'Timothy', 'Choco', 'Lily', 'Léo', 'Glagla']
print(family)
random=[3.14, 7, -2+1j, 'baguette', True, ['oui', 1], 5, 'Hello', 'Hi', 7, 'e']
print(len(random))
print(random[1::3])
print(random[5][1])

#Exercice 3
n=int(input("Enter an integer: "))
list=[]
for i in range (1, n+1):
    list.append(1/i)
#print(round(sum(list), 2))
sn=sum(list)
print("For n={} the sum accumulator is equal to {:.2f}".format(n, sn))

#Exercice 3
line=input("Enter, in a single line and separated by spaces, the desired temperature values:\n ")
smooth_txt=line.split()
print("List is now : {}".format(smooth_txt))
temp=[]
for element in smooth_txt:
    value=float(element)
    temp.append(value)
print("The final list is{}".format(temp))

#Exercice 4
a=[1, 3, 5, 7, 11]
b=[13, 17]
c=a+b
print("First instruction print: {}".format(c))
b[0]=-1
d=[]
for e in a:
    d.append(e+1)
print("Second instruction print: {}".format(d))
d.append(b[0]+1)
d.append(b[-1]+1)
print(f"Third instruction print {d[-2:]}")
print(f"Fourth instruction print {d[:-1]}")
print(f"Fifth instruction print {d[1:4]}")

#Exercice 5
n=int(input("Enter an integer: "))
list_num=[]
for i in range(n+1):
    list_num.append(i**2)
    
#Exercice 6
student_name=input("Enter student name: ")
name_list=[]
name_list.append(student_name)
grade_list=[]
cnt=1
while student_name!='':
    score=int(input("Enter grade out of 10: "))
    grade_list.append(score)
    student_name=input("Enter student name: ")
    name_list.append(student_name)
    cnt+=1
for i in range (len(name_list)-1):
    print(name_list[i],": ", grade_list[i])
average=sum(grade_list)/cnt
print(round(average, 2))









