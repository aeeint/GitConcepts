# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:36:34 2023

@author: Teanie
"""

names=open(r"Desktop\Python_ie\txt_files\names.txt", "r")
print(names)
for name in names:
    print("Hello {}".format(name))
    
    
f_names=open(r"Desktop\Python_ie\txt_files\names.txt", "r")
print(names)
for name in f_names:
    name=name.strip()
    print("Hello {}".format(name))
    
    
file=open(r"Desktop\Python_ie\txt_files\names.txt", "r")
for name in file:
    if "a" in name:
        name=name.strip()
        print("Hello {}".format(name))
        

#The basics:
# f=open(r"test.txt", "r") #reading
f=open(r"Desktop\Python_ie\txt_files\names.txt", "w") #writing
#f =open("test.txt", "a") #appending
# f=open(r"test.txt", "r+") #reading & writing
print(f.name)
#f.close()


fnames=open(r"Desktop\Python_ie\txt_files\names.txt", "r")
for name in fnames:
    print(name)
    
fnames=open(r"Desktop\Python_ie\txt_files\names.txt", "w")#do not use if not mofifying the file
for name in fnames:
    print(name)
    
    
#Reading a file (Context Manager)
with open(r"Desktop\Python_ie\txt_files\names.txt", "r") as f:
    pass

with open(r"Desktop\Python_ie\txt_files\names.txt", "r") as f:
    #Small files:
    f_contents=f.read()
    print(f_contents)


with open(r"Desktop\Python_ie\txt_files\names.txt", "r") as f:
    #Big files:
    f_contents=f.readlines()#read all lines and put as a list
    print(f_contents)
    

with open(r"Desktop\Python_ie\txt_files\names.txt", "r") as f:
    #With the extra lines:
    f_contents=f.readline()#read one lines at a time
    print(f_contents, end=" ")
    f_contents=f.readline()
    print(f_contents, end=" ")
    f_contents=f.readline()
    print(f_contents, end=" ")

#writing files
with open(r"names2.txt", "w") as f:#if names2.txt does not exist, it will create a new files
    f.write("Test")

##Writing starts:
with open(r"test.txt", "w") as f:
    f.write("Hello world")
    f.seek(0)#find the character with index i
    f.write("R")#and replace it with the character x

with open(r"test2.txt", "w") as f:#open takes strings 
    val1='names'#so values can only be string
    val2='niamh'
    val3='10'
    f.write(val1+'\t'+val2+'\t')#'\t' to put a space 
    f.seek(0)
    f.write("Test")
    f.seek(6)
    f.write("z")

#Copying files
with open(r"test.txt", "r") as rf:
    with open(r"test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)


#Copying an image
with open(r"Geto_bebou.jpg", "rb") as rf:#b is for bytes
    with open(r"Geto_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)










