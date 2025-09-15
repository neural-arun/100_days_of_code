import random

# Use a dictionary to store choices for easy lookup
# This is cleaner than three separate variables.
choices = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissor": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Define the winning combinations in a dictionary.
# The key beats its corresponding value.
win_conditions = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

# Get computer's choice
computer_choice_name = random.choice(list(choices.keys()))

# --- INPUT VALIDATION LOOP ---
# Keep asking the user until they enter a valid choice.
while True:
    user_choice_name = input("Enter your choice (rock/paper/scissor): ").lower()
    if user_choice_name in choices:
        break  # Exit the loop if the input is valid
    else:
        print("Invalid choice! Please enter rock, paper, or scissor.")

# --- DISPLAY CHOICES ---
print("\nComputer chose:")
print(choices[computer_choice_name])

print("\nYou chose:")
print(choices[user_choice_name])

# --- DETERMINE WINNER ---
if user_choice_name == computer_choice_name:
    print("It's a tie! 🤝")
# Check if the user's choice beats the computer's choice
elif win_conditions[user_choice_name] == computer_choice_name:
    print("You win! 🎉")
else:
    print("Computer wins! 💻")