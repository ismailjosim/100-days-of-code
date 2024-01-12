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

print(type(number_char)) # <class 'int'>

# type conversion
newNumChar = str(number_char) # num to char/string

print("Your name has " + newNumChar + " characters") # Output => Your name has 6 characters

# similar
float(70 + float("100.5")) # => output: 170.5 convert string to number then add them
