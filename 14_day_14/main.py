from art import logo
print("Welcome to:")
print(logo)
from game_data import data

import random

choiceB = random.choice(data)


score = 0
is_game_end = False
while not is_game_end:
    choiceA = choiceB
    print(f"Choice A: {choiceA["name"]}, a {choiceA["description"]} from {choiceA["country"]}.")
    from art import vs
    print(vs)
    choiceB = random.choice(data)
    print(f"Choice B: {choiceB["name"]}, a {choiceB["description"]} from {choiceB["country"]}.")
    print(f"A: {choiceA["follower_count"]}")
    print(f"B: {choiceB["follower_count"]}")
    guess = input("Guess who has more follower(A/B)? ").lower()

    def compare_follower_count():
        #compares the followers count,returns celebrity who has more followers
        if choiceA["follower_count"] > choiceB["follower_count"]:
            return "a"
        elif choiceA["follower_count"] < choiceB["follower_count"]:
            return "b"

    if guess == compare_follower_count():
        score += 1
        print(f"You are correct, your score is {score}.")

        
    else:
        is_game_end = True
        print(f"Sorry! you got it wrong this time, your final score is {score}.")