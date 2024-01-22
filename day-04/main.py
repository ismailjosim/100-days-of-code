# import random module
import random
import secret_key

# generate random round number between 1-10 (whole number)
number = random.randint(1, 10)
# print(number)

# import code from module
print(secret_key.secretKey)

# random floating point number
print(random.random())

# random float number from 1 to 10
randomValue = random.random()
print(randomValue * 10)

# Coding Exercise #1: HEADS OR TAILS
import random
randomValue = random.randint(0,1)

if(randomValue == 1):
    print("Heads")
else:
    print("Tails")

# List in python [similar to array in JS]
city = ["Dhaka","Chittagong","Khulna","Rajshahi","Barisal","Sylhet","Rangpur","Mymensingh"]
city[1] = "Chattogram"

print(city)


# add item at the end of the list
city.append("Noakhali")
print(city)
