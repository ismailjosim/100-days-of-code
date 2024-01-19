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

# year = int(input("Enter Year "))

# # My solution
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# # MULTIPLE IF STATEMENTS
# height = int(input("Enter Your Heigh in CM: "))
# bill = 0

# if(height >120):
#     age = int(input("Enter Your age: "))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12
#     take_photo = input("Do you want to take photo? Y or N ")
#     if(take_photo == "Y"):
#         bill += 3
#     print(f"Your Final bill is {bill}")
# else:
#     print("can't ride")

# CODING CHALLENGE #5: lOVE CALCULATOR

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

personOne = name1.upper()
personTwo = name2.upper()


countOne = 0
countTwo = 0

# True count for person one
nameCharOne = personOne.count('T')
nameCharTwo = personOne.count('R')
nameCharThree = personOne.count('U')
nameCharFour = personOne.count('E')


# love count for person one
nameChar2One = personOne.count('L')
nameChar2Two = personOne.count('O')
nameChar2Three = personOne.count('V')
nameChar2Four = personOne.count('E')

countOne = nameCharOne + nameCharTwo + nameCharThree + nameCharFour
countTwo = nameChar2One + nameChar2Two + nameChar2Three + nameChar2Four

# True count for person one
name2CharOne = personTwo.count('T')
name2CharTwo = personTwo.count('R')
name2CharThree = personTwo.count('U')
name2CharFour = personTwo.count('E')


# love count for person one
name2Char2One = personTwo.count('L')
name2Char2Two = personTwo.count('O')
name2Char2Three = personTwo.count('V')
name2Char2Four = personTwo.count('E')

countOne += name2CharOne + name2CharTwo + name2CharThree + name2CharFour
countTwo += name2Char2One + name2Char2Two + name2Char2Three + name2Char2Four


total = str(countOne) + str(countTwo)
loveSore = int(total)


if loveSore < 10 or loveSore > 90:
    print(f"Your score is {loveSore}, you go together like coke and mentos.")
elif loveSore > 40 and loveSore < 50:
     print(f"Your score is {loveSore}, you are alright together.")
else:
    print(f"Your score is {loveSore}.")


