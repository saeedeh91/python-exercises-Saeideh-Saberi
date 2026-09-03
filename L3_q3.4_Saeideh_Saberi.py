'''
session-03 

q3.4

-----------<Student score>--------------

'''

score = int(input("enter the Score:"))


if 18 <= score <= 20:
        print("score is A***")
elif 16 <= score < 18:
        print("score is B**")
elif 14 <= score < 16:
        print("score is C*")
elif 10 <= score < 14:
        print("score is D")
else:
    print("score is F")
    print("You are failed")