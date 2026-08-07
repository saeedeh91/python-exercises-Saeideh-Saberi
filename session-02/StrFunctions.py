# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:38:53 2026

@author: Saeideh


saeideh saberi

Python - 07 - houzouri 

 Second Session ---- My Second Coding Exercise - StrFunctions
"""


name = 'saeideh'
cap_name = name.capitalize()

print('capitalize the name:', cap_name) #capitalize the name: Saeideh
#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------
name2 = 'SABERI'

casef_name = name.casefold()

print("casefold the name:", casef_name) #casefold the name: saeideh

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

centr_name = name.center(20,'<') # center(length, character) | default is space

print('return the centered string:', centr_name)# return the centered string: <<<<<<saeideh<<<<<<<

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

cont_name = name.count('s')

print('number of times, it occurs:',cont_name) #number of times, it occurs: 1

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


encde = name.encode()#encode(encoding = '', errors = '')

print('the encoded string is:', encde) #the encoded string is: b'saeideh'

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

eswtch = name.endswith('e')

print('the status is:', eswtch) # the status is: False

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

text = 'Saeideh\tSaberi\tStudent' #\t
tabs = text.expandtabs(10)
tabs2 = text.expandtabs(20)
print('the tab size is:', tabs) #the tab size is: Saeideh   Saberi    Student


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


fname = name.find('e',3,6) # string.find(value, start, end)

print('output of find function:', fname) #output of find function: 5

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

ftext = 'saeide is {}' 
for_name = ftext.format(35) # {palceholders}--> method formats the specified value(s) and insert them inside the string's placeholder
print('format the name:', for_name) # format the name: saeide is 35


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


dic_saeideh = {"lastname": "Saberi", "Age": 35, "number": 1234567890}
map_txt = "her lastname is {lastname}. she is {Age}  and her number is {number}"
newtext = map_txt.format_map(dic_saeideh)

print('map format is:', newtext)# map format is: her lastname is Saberi. she is 35  and her number is 1234567890

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


in_name = name.index('i')#return the position of specified value
print('the index function: ', in_name)# the index function:  3

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


alphanum = name.isalnum()
print("the function of isalnum:", alphanum) # the function of isalnum: True

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------
s1= '2324345345'
alpha1= s1.isalpha()
print("the function of isalpha:",alpha1)  # the function of isalpha: False //////if not in alphabet

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


askii = name.isascii()
print('the function of ascii:', askii) #the function of ascii: True


desimal = name.isdecimal()	
print('thefunction of decimal:', desimal)   # thefunction of decimal: False

s1 = '45645657567'
s2 = 'saeideh saberi'

s11 = s1.isdigit()
print('the function of isdigit', s11) # the function of isdigit True

s12 = s2.isidentifier()
print('the function of isidentifier',s12) # the function of isidentifier False

s3 = 'saboori'
s13 = s3.isidentifier()
print('the function of identifier2:', s13) # the function of identifier2: True
 

s14 = s3.islower()
print('the function of islower:', s14) #the function of islower: True

s15 = s3.isprintable()
print('the function of isprintable:', s15) # the function of isprintable: True

ss = 'hello_|saeideh'
s16 = ss.isprintable()
print('the function of isprintable1:', s16) # the function of isprintable1: True

s17 = ss.istitle()# returns True if all words in a text start with a upper case letter
print('the function of istitle:', s17) # the function of istitle: False

s18 = ss.isupper()# Returns True if all characters in the string are upper case
print('the function of isupper:', s18) #the function of isupper: False

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


mytuple = ("saeide"," is 35"," and lives in Tehran")

x = ''.join(mytuple) # این متد برای اتصال چند رشته (String) به یکدیگر با استفاده از یک جداکننده (Separator) استفاده می‌شود.

print('the join result is:',x) #saeide is 35 and lives in Tehran

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


s19 = name.ljust(20,'*') # The original string is left-justified within the new string, and the remaining space on the right is filled with a specified character
print('the function of ljust:', s19) # the function of ljust: saeideh*************

b = '               saeidh_saberii'
s20 = b.lstrip()
print('the lstrip result is:',s20) # saeidh_saberii


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

c = "i live in germany         "
               
tbl = str.maketrans("germany", "abcdedd")
result = c.translate(tbl)
print('the maketrans result is:', result)# the result is: i livb id abcdedd


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


r1 = c.partition('germany') # searches for a specified string, and splits the string into a tuple containing three elements
 
print("partition result is:", r1) # result is: ('i live in ', 'germany', '')

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r2 = c.replace('germany', 'spain')
print("replace result is:", r2) # result is: i live in spain

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r3 = c.rfind('i')

print("rfind result is:", r3) # result is: 4  (v)    //// result is: 7 (i)


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r4 = c.rindex('g')

print("rindex result is:", r4) # result is: 10

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r5 = c.rjust(30, '-')# will right align the string, using a specified character (space is default) as the fill character.
print("rjust result is:", r5) # result is: -------------i live in germany


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r6 = c.rpartition('live') 
print("rpartition result is:", r6) # result is: ('i ', 'live', ' in germany')

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r7 = c.rsplit() # method splits a string into a list, starting from the right
print("rsplit result is:", r7)# result is: ['i', 'live', 'in', 'germany']

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

c1 = "python*&^%*"
r8 = c1.rstrip('*&^%*')
print('the rstrip result is:', r8)#the result is: python


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


r9 = c.startswith('r')
print('the startswith result is:', r9)#the result is: False

r10 = c.startswith('e', 5 ,10) # string.startswith(value, start, end)
print('the startswith result is:', r10)# the result is: True


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

txtt= " .........i eat breakfast everyday -------------- rrrr"
r10 = txtt.strip(".- r")# فقط از ابتدا و انتهای رشته حذف می‌کند، نه از وسط آن
print('the strip result is:', r10)#the result is: i eat breakfast everyday

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


r11 = c.swapcase()
print('the swapcase result is:', r11)#the result is: I LIVE IN GERMANY 

#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------


r12 = c.title()

print('the title result is:', r12) # the result is: I Live In Germany 


#--------------------------------
# ||||||||||||||||||||||||||||||||||||
#--------------------------------

r13 = c.zfill(30)
 
print('the zfill result is:', r13)# the result is: 0000i live in germany  

