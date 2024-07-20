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

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(display)
    if "_" not in display:
        end_game = True
        print("You Win.")





