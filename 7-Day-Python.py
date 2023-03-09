

# import random
#
# word_list = ["ardvark", "baboon", "camel"]
#
# chosen_word = random.choice(word_list)
#
# guess = input("Guess a letter:").lower()
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

import random

word_list = ["banana", "apple", "orange"]

choice_word = random.choice(word_list)

print(f"{choice_word}")


import random

word_list = ["banana", "apple", "orange"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")




