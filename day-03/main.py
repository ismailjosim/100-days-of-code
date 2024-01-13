# Conditional Statement (if-else statement)\

""" PYTHON IF-ELSE SYNTAX
if condition:
    do this
else:
    do this
"""

height = int(input("Enter Your Heigh in CM: "))

if height > 120:
    print("Here is your ticket!")
else:
    print("Sorry! your height is not enough to get the ticket!")

""" Comparison Operators
    1. > greater then
    2. < less then
    3. >= greater then or equal to
    4. <= less then or equal to
    5. == equal to
    6. != not equal to
"""

# Coding Challenge: 01
number = int(input())

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Nested if-else statement
""" PYTHON IF-ELSE SYNTAX
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""

height = int(input("Enter Your Heigh in CM: "))


if(height >120):
    print("You can Ride the rollercoaster ride")
    age = int(input("Enter Your age: "))
    if age < 12:
        print("Can pay $5 ticket")
    elif age <= 18:
        print("Can pay $7 ticket")
    else:
        print("Can pay $12 ticket")
else:
    print("can't ride")
