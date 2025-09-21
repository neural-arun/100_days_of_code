import random
print("Hello and Welcome to Blackjack Game!")

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(card)
    return card

user_cards = [deal_card() , deal_card()]
computer_cards = [deal_card() , deal_card()]

def calculate_score(player_score):
    return sum(player_score)

