import random

def get_user_choice():
    # Get user's choice of difficulty
    while True:
        choice = input("Choose a difficulty (easy/hard): ").lower()
        if choice in ['easy', 'hard']:
            return choice
        else:
            print("Invalid choice. Please enter 'easy' or 'hard'.")

def get_number_of_guesses(difficulty):
    # Determine the number of guesses based on difficulty
    if difficulty == 'easy':
        return 10
    else:
        return 5

def get_user_guess():
    # Get user's guess and ensure it's a valid integer
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, number):
    # Check if the guess is correct, too high, or too low
    if guess == number:
        return "Correct!"
    elif guess < number:
        return "Too low!"
    else:
        return "Too high!"

def main():
    # Main function to run the game
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    difficulty = get_user_choice()  # Get user's choice of difficulty
    max_guesses = get_number_of_guesses(difficulty)  # Determine the number of guesses
    print(f"You have {max_guesses} guesses to guess the number between 1 and 100.")

    for guess_count in range(1, max_guesses + 1):
        print(f"\nGuess {guess_count}:")
        guess = get_user_guess()  # Get user's guess
        result = check_guess(guess, number)  # Check the guess
        print(result)

        if result == "Correct!":
            print(f"Congratulations! You guessed the number in {guess_count} guesses.")
            break
    else:
        print(f"Sorry, you've run out of guesses. The number was {number}.")

if __name__ == "__main__":
    main()
    
