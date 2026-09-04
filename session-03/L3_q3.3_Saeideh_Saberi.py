'''
session-03 

q3.3

-----------<calculator>--------------

'''

num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
operation = input('determine the oprator to calculate:') #-, +, *, /


if operation == '+':
    jam = num1 + num2
    print("sum is:", jam)
elif operation == '-':
    tafrigh = num1 - num2
    print("sum is:", tafrigh)
elif operation == '*':
        zarb = num1 * num2
        print("sum is:", zarb)
elif operation == '/':
        taghsim = num1 / num2
        print("sum is:", taghsim)
else:
    print("it is not an operator")