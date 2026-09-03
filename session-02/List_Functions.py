# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:40:17 2026

@author: Saeideh

saeideh saberi

Python - 07 - houzouri 

 Second Session ---- My Second Coding Exercise - list_functions
"""

saeide_List = ["tehran", "karaj", "esfahan" , "shiraz" , "yazd"]
saeide_List2 = ["A", "B", "C"]
list3 = ['14', '19', '20']

saeide_List.append("kermanshah")
print("the append result is:", saeide_List) #the result is: ['tehran', 'karaj', 'esfahan', 'shiraz', 'yazd', 'kermanshah']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

saeide_List2.clear()
print("the clear result is:", saeide_List2)# the result is: []
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

c = saeide_List.copy()
print("the copy result is:", c) #the result is: ['tehran', 'karaj', 'esfahan', 'shiraz', 'yazd', 'kermanshah']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

c2 = saeide_List.count('tehran')
print("the count result is:", c2) # the count result is: 1
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
saeide_List.extend(list3)
print("the extend result is:", saeide_List) # the extend result is: ['tehran', 'karaj', 'esfahan', 'shiraz', 'yazd', 'kermanshah', '14', '19', '20']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    

i = list3.index('20')
print("the index result is:", i)# the index result is: 2
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

list3.insert(0,'345')# (position, "str value")
print("the insert result is:", list3)# the index result is: ['345', '14', '19', '20']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

saeide_List.pop(3)
print("the pop result is:", saeide_List) # the pop result is: ['tehran', 'karaj', 'esfahan', 'kermanshah', '14', '19', '20']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
saeide_List.remove("karaj")
print("the remove result is:", saeide_List) #the remove result is: ['tehran', 'esfahan', 'kermanshah', '14', '19', '20']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
saeide_List.sort()
print("the sort result is:", saeide_List) # the sort result is: ['14', '19', '20', 'esfahan', 'kermanshah', 'tehran', 'yazd']

