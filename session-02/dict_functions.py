# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:30:24 2026

@author: Saeideh

Second Session ---- My Second Coding Exercise - Dict_functions
"""


mydict = {"name":"saeideh", "lname": "saberi", "age": 35 , "place": "tehran"}

herdict = {"a": "apple", "b": "ball", "c":"cellphone"}

a = herdict.copy()
print("the copy result is:", a)# the copy result is: {'a': 'apple', 'b': 'ball', 'c': 'cellphone'}


b = ('sh', 'chh', 'pwa')
d = 4
newdict = dict.fromkeys(b , d)# returns a dictionary with the specified keys and the specified value.
print("the fromkeys result is:", newdict)# the fromkeys result is: {'sh': 4, 'chh': 4, 'pwa': 4}


e = herdict.get('b')
print ('the get result is:',e)# the get result is: ball

g = mydict.items() # The view object contains the key-value pairs of the dictionary, as tuples in a list
print ('the items result is:',g) # the items result is: dict_items([('name', 'saeideh'), ('lname', 'saberi'), ('age', 35), ('place', 'tehran')])


h = mydict.keys()
print('the keys result is:',h) #the keys result is: dict_keys(['name', 'lname', 'age', 'place'])


herdict.pop("b")
print('the pop result is:',herdict)# the pop result is: {'a': 'apple', 'c': 'cellphone'}



mydict.popitem()
print('the popitem result is:',mydict) # the popitem result is: {'name': 'saeideh', 'lname': 'saberi', 'age': 35}

mydict.update({"place":"tehran"})
print("the update result is:", mydict)#the update result is: {'name': 'saeideh', 'lname': 'saberi', 'age': 35, 'place': 'tehran'}


j = herdict.setdefault("b","banana")
print('the setdefault result is:', j)# the setdefault result is: banana
print ("the new herdict:", herdict)# the new herdict: {'a': 'apple', 'c': 'cellphone', 'b': 'banana'}

v = mydict.values()
print('the values resut is:', v) # the values resut is: dict_values(['saeideh', 'saberi', 35, 'tehran'])


herdict.clear()
print('the clear result is:', herdict) # the clear result is: {}
