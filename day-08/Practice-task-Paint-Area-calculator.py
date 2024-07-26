import math


def paint_calc(height, width, cover):
    result = math.ceil((height * width)/cover)
    print(f"You'll need {result} cans of paint.")








# 🚨 Don't change the code below 👇
test_h = int(input("Enter height In meter: ")) # Height of wall (m)
test_w = int(input("Enter width In meter: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
