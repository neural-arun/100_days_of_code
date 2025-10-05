print("Hello and Welcome to Number guessing Game!")
import random
answer = random.randint(1,100)
print("the answer is ",answer)

def easy_or_hard():
    level = input("Enter 'easy' for Easy level and 'hard' for Hard level: ")
    if level == "easy":
        return 10
    else:
        return 5
def game():
    attempts = easy_or_hard()
    print(f"You have {attempts} attempts, lets play the game.")
    while attempts > 0:
        turn = int(input("Enter Your Guess: "))
        if turn == answer:
            print("Congratulations! you got it correct.")
            break
        elif turn > answer:
            attempts -= 1
            print("Too High!")
            print(f"You have {attempts} attempts left.")
        else:
            attempts -= 1
            print("Too low!")
            print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print("Sorry, You have utilised all your attempts, to play again restart the game.")
    restart = input("Do you want to restart the game(y/n): ")
    if restart == "y":
        game()
    elif restart == "n":
        print("Thanks for playing the game!, come again next time.")
game()