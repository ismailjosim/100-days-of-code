# # Conditional Statement (if-else statement)\

# """ PYTHON IF-ELSE SYNTAX
# if condition:
#     do this
# else:
#     do this
# """

# height = int(input("Enter Your Heigh in CM: "))

# if height > 120:
#     print("Here is your ticket!")
# else:
#     print("Sorry! your height is not enough to get the ticket!")

# """ Comparison Operators
#     1. > greater then
#     2. < less then
#     3. >= greater then or equal to
#     4. <= less then or equal to
#     5. == equal to
#     6. != not equal to
# """

# # Coding Challenge: 01
# number = int(input())

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# # Nested if-else statement
# """ PYTHON IF-ELSE SYNTAX
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this
# """

# height = int(input("Enter Your Heigh in CM: "))


# if(height >120):
#     print("You can Ride the rollercoaster ride")
#     age = int(input("Enter Your age: "))
#     if age < 12:
#         print("Can pay $5 ticket")
#     elif age <= 18:
#         print("Can pay $7 ticket")
#     else:
#         print("Can pay $12 ticket")
# else:
#     print("can't ride")


# # Coding Challenge #3: BMI calculation 2.0
# height = float(input())
# weight = int(input())

# calcBMI = weight / height ** 2

# # my solution
# if calcBMI > 18.5:
#     if (calcBMI > 18.5 and calcBMI < 25): # if calcBMI over 18 and below 25
#         print(f"Your BMI is {calcBMI}, you have a normal weight.")
#     elif(calcBMI >= 25 and calcBMI < 30): # if calcBMI Equal or over 25 and below 30
#         print(f"Your BMI is {calcBMI}, you are slightly overweight.")
#     elif(calcBMI >= 30 and calcBMI < 35): # if calcBMI Equal or over 30 and below 35
#         print(f"Your BMI is {calcBMI}, you are obese.")
#     else:
#         print(f"Your BMI is {calcBMI}, You are clinically obese.")
# else:
#     print(f"Your BMI is {calcBMI}, You are underweight.")

# # alternative solution
# if calcBMI < 18.5:
#      print(f"Your BMI is {calcBMI}, You are underweight.")
# elif calcBMI < 25:
#     print(f"Your BMI is {calcBMI}, you have a normal weight.")
# elif calcBMI < 30:
#     print(f"Your BMI is {calcBMI}, you are slightly overweight.")
# elif calcBMI < 35:
#     print(f"Your BMI is {calcBMI}, you are obese.")
# else:
#     print(f"Your BMI is {calcBMI}, You are clinically obese.")

year = int(input("Enter Year "))

# My solution
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

