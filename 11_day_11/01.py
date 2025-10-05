import random
def deal_card():
    """ return a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
user_cards = []
computer_cards = []
for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)
def compare(user_score , computer_score):
    if user_score == computer_cards:
        return "It's a Draw"
    elif user_score == 0:
        return "You got a blackjack, You win!"
    elif computer_score == 0:
        return "opponent got a blckjack , you lose"
    elif computer_score < user_score :
        return "You win"
    elif user_score > 21:
        return "You busted!"
    elif computer_score >21:
        return "computer busted , You win!"
    elif computer_score > user_score:
        return "You lose"
user_score = 0
computer_score = 0
is_game_over = False
def paly_game():
    
    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} , current score {user_score}")
        print(f"computer's first card: {computer_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score> 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, Type 'n' to pass? ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


final_compare = compare(user_score , computer_score)
print(final_compare)
print(f"Your hand: {user_cards}, Your score: {user_score}")
print(f"computer's hand: {computer_cards}, computer score: {computer_score}")




while is_game_over == True:
    should_play_game = input("Do you want to play blackjack(y/n)? ")
    if should_play_game == "y":
        paly_game()
