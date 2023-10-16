# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:17:31 2023

@author: Teanie
"""

#To declare a function:
    #def function_name(arguments):
        #statement
        
#to create a dictionary
country_capitals={
       "United states": "Washington DC",
       "Italie": "Rome",
       "England": "London"}
print(country_capitals)
#data key can't be a list

dictionary={}
print(dictionary)
#to create an empty dictionary

Dict=dict({1: 'Geeks', 2:'For', 3:'Geeks'})
print(Dict)

#creating a nested dictionary (dictionary in dictionary)
Dictio={1: 'Geeks', 2:'For', 3:{'A':'Welcolme', 'B': 'To', 'C': 'Geeks'}}
print(Dictio[3]['A'])

#We can't change the key but we can change the values
country_capitals["Italie"]='Naples'
print(country_capitals)

#to add an item
country_capitals={
       "United states": "Washington DC",
       "Italie": "Rome",
       "England": "London"}
print("before: ", country_capitals)
country_capitals['Germany']='Berlin'
print("after: ", country_capitals)
del country_capitals['United states']
#to delete an item
print("after removing USA: ", country_capitals)
country_capitals.clear()
#to remove all of the items
print("after clearing: ", country_capitals)

my_list={1:'Hello', 2: 'Hi', 'Howdy':100}
print(1 in my_list)
print('Howdy' not in my_list)
print('Hello' in my_list)
#check if key exists 

#demo for all dictionary methods
dict1={1:"Pyhton", 2:"Java", 3:"Ruby", 4:"Scala"}
dict2=dict1.copy()
print(dict1.items())
print(dict1.keys())
print(dict1.values())
dict2.update({3:"Scala"})
print(dict2.pop(4))
dict2.popitem()
print(dict2)

cities=['Paris', 'Athens', 'Madrid']
country=['France', 'Greece', 'Spain']
continent='Europe'
my_dictionary=dict(zip(cities, country))
print(my_dictionary)


#Exercice 1
dictionary={}
list1=['Ten', 'Twenty', 'Thirty']
list2=[10, 20, 30]
for i in range(len(list1)):
    dictionary[list1[i]]=list2[i]
print(dictionary)
#or
dictionary=dict(zip(list1, list2))
print(dictionary)


#Exercice 2
#create a dictionary out of 2 dictionary
dict1={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2={'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
#or
dict3={**dict1, **dict2}
print(dict3)


#Exercice 3
sampleDict={"class":{"student": {"name": "Mike", "marks":{"physics":70, "history":80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])


#Exercice 4
employees=['Kelly', 'Emma']
defaults={"designation": 'developer', "salary":8000}
res=defaults.fromkeys(employees, defaults)
print(res)
print(res['Kelly'])


#Exercice 5
sample_dict={"name": "Kelly", "age":25, "salary":8000, "city":"New York"}
del sample_dict["name"]
del sample_dict["salary"]
print(sample_dict)
#or
sample_dict.pop("name")
sample_dict.pop("salary")
print(sample_dict)


#Exercice 6
sample_dict={'a': 100, 'b': 200, 'c':300}
if 200 in sample_dict.values():
    print("200 present in a dict")


#Exercice 7
sample_dict={'emp1': {'name':'Jhon', 'salary':7500}, 'emp2':{'name':'Emma', 'salary':8000}, 'emp3':{'name':'Brad', 'salary':500}}
sample_dict.update({'emp3':{'name':'Brad', 'salary':8500}})
print(sample_dict)
#or
sample_dict['emp3']['salary']=8500
print(sample_dict)




































