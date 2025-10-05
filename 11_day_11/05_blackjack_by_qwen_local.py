import random

# Define card values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Initialize deck
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
random.shuffle(deck)

def calculate_hand_value(hand):
    """Calculate the value of a hand."""
    value = sum(10 if card['rank'] in ['Jack', 'Queen', 'King'] else 11 if card['rank'] == 'Ace' else int(card['rank']) for card in hand)
    # Adjust for Aces
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def print_hand(hand, message):
    """Print a hand with a message."""
    print(message)
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total: {calculate_hand_value(hand)}\n")

# Initial deal
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

print_hand(player_hand, "Your Hand:")
print_hand(dealer_hand, "Dealer's Hand (One Card):")

# Player's turn
while True:
    action = input("Do you want to Hit or Stand? ").lower()
    if action == 'hit':
        player_hand.append(deck.pop())
        print_hand(player_hand, "Your Hand:")
        if calculate_hand_value(player_hand) > 21:
            print("Bust! You lose.")
            break
    elif action == 'stand':
        break
    else:
        print("Invalid input. Please type Hit or Stand.")

# Dealer's turn
if calculate_hand_value(player_hand) <= 21:
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print_hand(dealer_hand, "Dealer's Hand:")

# Determine the winner
player_score = calculate_hand_value(player_hand)
dealer_score = calculate_hand_value(dealer_hand)

if player_score > 21:
    print("You bust! You lose.")
elif dealer_score > 21:
    print("Dealer busts! You win!")
elif player_score == dealer_score:
    print("It's a tie!")
elif player_score > dealer_score:
    print("You win!")
else:
    print("Dealer wins!")

# Reset the deck for the next game
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
random.shuffle(deck)
