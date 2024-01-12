# Data Types

# String (Subscription)
print("Hello"[2])
print("Hello"[4])

# Number (Int)
print(123 + 456)

# Number (float)

print(3.14156)

# Boolean
True
False

# Type check
number_char = len(input("What is your name?\n"))
print("Your name has " + number_char + " characters") # output => TypeError: can only concatenate str (not "int") to str

print(type(number_char)) # output <class 'int'>

# type conversion
newNumChar = str(number_char) # num to char/string

print("Your name has " + newNumChar + " characters") # Output => Your name has 6 characters

# similar
float(70 + float("100.5")) # => output: 170.5 convert string to number then add them

# # Coding Challenge: DATA TYPES
# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
b = int(two_digit_number[0])
c = int(two_digit_number[1])
print(b+c)


# mathematical operators
3 + 7
5-3
3*2
6/3

# 2**3 = 8 power

# give priority PEMDAS => (),**, * /, + -

print(3 * 3 + 3 / 3 - 3) # 6
"""
# ==> Steps
        Multiply (3 * 3) = 9 Division (3/3) = 1.0
        Add 9 + 1.0 = 10.0
        Subtraction 10.0 - 3 = 7.0
"""

# Challenge change the above math order so that it can print 3.0
print(3 * (3 + (3 / 3) - 3))
# alternative
print(3 * (3 + 3) / 3 - 3)


height = input()
weight = input()

heightFloat = float(height)
weightNum = int(weight)

# My solution
bmiCalculator = round(weightNum / (heightFloat * heightFloat))

# Alternative Solution
bmiCalculator = round(weightNum / heightFloat ** 2)
print(bmiCalculator)

# float division
print(8 // 3) # 2


# shorthand
# +=
# -=
# ++

# F-string
name = "Ismail"
age = 25
height = 1.75
isMarried = "Single"
isStudent = False


# f STRING syntax = f"Your score is {}"

print(f"Person Name is {name}. Age {age} Years old. Currently {isMarried}. Student Roll is: {isStudent}")
