# # import random module
# import random
# import secret_key

# # generate random round number between 1-10 (whole number)
# number = random.randint(1, 10)
# # print(number)

# # import code from module
# print(secret_key.secretKey)

# # random floating point number
# print(random.random())

# # random float number from 1 to 10
# randomValue = random.random()
# print(randomValue * 10)

# # Coding Exercise #1: HEADS OR TAILS
# import random
# randomValue = random.randint(0,1)

# if(randomValue == 1):
#     print("Heads")
# else:
#     print("Tails")

# # List in python [similar to array in JS]
# city = ["Dhaka","Chittagong","Khulna","Rajshahi","Barisal","Sylhet","Rangpur","Mymensingh"]
# city[1] = "Chattogram"

# print(city)


# # add item at the end of the list
# city.append("Noakhali")
# print(city)



# # Coding Exercise #2: Banker Roulette
# import random
# names_string = input()

# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# randomValue = round(random.randint(0,len(names)-1))
# pickRandomPerson = names[randomValue]
# print(f"{pickRandomPerson} is going to buy the meal today!")

# city = ["Dhaka","Chittagong","Khulna","Rajshahi","Barisal","Sylhet","Rangpur","Mymensingh"]
# print(city[9]) # IndexError: list index out of range

# Nested List
# city = [["Dhaka","Chittagong","Khulna","Rajshahi"],["Barisal","Sylhet","Rangpur","Mymensingh"]]
# print(city)

# # Coding Exercise #3: Banker Roulette
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ['a','b','c']
# letterIndex = abc.index(letter)
# numberIndex = int(position[1]) - 1
# map[numberIndex][letterIndex] = "x"


# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

# 🚀 Project: Rock Paper Scissors
import random

choices = ["Rock", "Paper", "Scissors"]
user_choice = input("Write one in letters: (🪨, 📄, ✂️) ").capitalize()

generate_random_number = random.randint(0, len(choices) - 1)
comp_choice = choices[generate_random_number]

if comp_choice == user_choice:
    print(f"It's a tie! Both chose {user_choice}.")
elif (
    (user_choice == "Rock" and comp_choice == "Scissors") or
    (user_choice == "Scissors" and comp_choice == "Paper") or
    (user_choice == "Paper" and comp_choice == "Rock")
):
    print(f"You win! {user_choice} beats {comp_choice}.")
else:
    print(f"You lose! {comp_choice} beats {user_choice}.")
