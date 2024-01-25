phoneBrand = ["apple", "SamSang","Nokia","Xiaomi"]

for brand in phoneBrand:
    print(brand)

# 💪 COding Challenge 01 :  AVERAGE HEIGHT

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height = 0
for student in student_heights:
  height += student

avg = round(height / len(student_heights))

print(f"total height = {height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {avg}")

# 💪 COding Challenge 02 : Find the height value

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
heightValue = 0
for value in student_scores:
  if value > heightValue:
    heightValue = value

print(f"The highest score in the class is: {heightValue}")

# for loops and the range() function: find total from 1 to 100
total = 0
for number in range(1, 101):
  total += number

print(total)

# 💪 COding Challenge 03 : ADDING EVEN NUMBERS

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
# My solution
total = 0
for number in range(1, target + 1):
  if(number % 2 == 0):
    total += number
print(total)

# alternative solution
for number in range(2, target + 1, 2):
  total += number

# 💪 Interactive Coding Exercise 04: The FizzBuzz Game

for number in range(1, 101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
