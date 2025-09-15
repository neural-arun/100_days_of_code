import random

scissor = '''
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

choices = [rock , paper , scissor]
computer_choice = random.choice(choices)

user_choice = input("Enter Your choice(rock/paper/scissor): ").lower()
if user_choice == "rock":
    user_choice = rock
elif user_choice == "scissor":
    user_choice = scissor
elif user_choice == "paper":
    user_choice = paper

print("Computer chose: ")
print(computer_choice)

print("You chose: ")
print(user_choice)

if computer_choice == user_choice:
    print("It's a tie")
elif computer_choice == rock and user_choice == scissor:
    print("Computer wins!")
elif computer_choice == rock and user_choice == paper:
    print("You win!")
elif computer_choice == paper and user_choice == rock:
    print("computer win!")    
elif computer_choice == paper and user_choice == scissor:
    print("You win!")
elif computer_choice == scissor and user_choice == rock:
    print("You win!")
elif computer_choice == scissor and user_choice == paper:
    print("Computer win!")
else:
    print("Something went wrong!")
