import random

# All functions are defined once at the top of the program.
# This makes them reusable.

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates and returns the score of a hand."""
    # Hint 7: Checks for a blackjack (Ace + 10) and returns 0.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Checks for an 11 (Ace) and changes it to a 1 if score is over 21.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares scores and determines the winner."""
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "The computer has a Blackjack. You lose!"
    elif user_score == 0:
        return "You have a Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "The computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

# --- The Main Game Loop ---

# Initial setup outside of the main game loop.
user_cards = []
computer_cards = []
game_end = False

# Hints 5: Deals the initial two cards.
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Hints 10 & 11: The game continues until game_end becomes True.
while not game_end:
    # Recalculates scores with every new card.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Hint 9: Checks for immediate end-game conditions.
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_end = True
    else:
        should_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            game_end = True

# Hint 12: The computer's turn happens AFTER the user's turn ends.
# This loop only runs if the game has not already ended (e.g., if the user didn't bust or get a Blackjack).
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

# Hint 13: Final score comparison and game result.
print("\nFinal Results:")
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))