import random
number = random.randint(1,100)
print("Hello and welcome to number guessing game!")
level = input("Type 'hard' for hard level and 'easy' for easy level: ")

def game_level(level):
    if level == "easy":
        attempts = 5
    else:
        attempts = 10
    for i in range(attempts):
        attempts -= 1
        guess = int(input("Enter guess: "))
        if guess == number:
            print("Congratulations, You got the number")
            break
        

### Got really sick after this it will be completed in later parts. 