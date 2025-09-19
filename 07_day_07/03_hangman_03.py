import random
word_list = ["ardvark" , "baboon" , "camel"]

chosen_word = random.choice(word_list)

print(f"chosen word is {chosen_word}")
word_length = len(chosen_word)
display = []
for letter in range(word_length):
    display += "_"
end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for positon in range(word_length):
        if guess == chosen_word[positon]:
            display[positon] = guess

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")
