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



# # Coding Exercise #1: Banker Roulette
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
city = [["Dhaka","Chittagong","Khulna","Rajshahi"],["Barisal","Sylhet","Rangpur","Mymensingh"]]
print(city)
