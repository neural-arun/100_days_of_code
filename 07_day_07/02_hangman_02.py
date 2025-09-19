
import random
word_list = ["ardvark" , "baboon" , "camel"]

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

print(f"chosen word is {chosen_word}")
word_length = len(chosen_word)
display = []
for letter in range(word_length):
    display += "_"


for positon in range(word_length):
    if guess == chosen_word[positon]:
        display[positon] = guess

print(display)



