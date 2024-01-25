phoneBrand = ["apple", "SamSang","Nokia","Xiaomi"]

for brand in phoneBrand:
    print(brand)

# COding Challenge 01 :  AVERAGE HEIGHT
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
