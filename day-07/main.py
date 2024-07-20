# step 01: Word collection
word_list= [ "ardvark", "baboon", "camel"]

# TODO 01: Randomly choose a word rom the word_list and assign it to a variable called chosen_word.

import random;
chosen_word = random.choice(word_list)
print(f"The random chosen word is: {chosen_word}")

# TODO 2: create an empty list called display.
#* for each letter in the chosen_word, add a "_" to 'display'.
#* so if the chosen_word is "apple", display should be ["_","_","_","_","_"]. with 5 "_" representing each letter to guess.
display = []

#* method 01
# for letter in chosen_word:
#     display += "_"

#* method 02
for l in range(len(chosen_word)):
    display+="_"

# TODO 3: Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase
guess = input("Guess a letter: ").lower()



# TODO 4: check if the letter user guessed (guess) is one of the letters in the chosen_word.
for pos in range(len(chosen_word)):
    letter = chosen_word[pos]
    if letter == guess:
        display[pos] = letter




print(display)
