import random
game_end = False

def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        first_card = random.choice(cards)
        return first_card

def calculate_score(player_sum):
        if sum(player_sum) == 21 and len(player_sum) == 2:
            return 0
        elif 11 in player_sum and sum(player_sum) >21:
            player_sum.remove(11) 
            player_sum.append(1)
            return sum(player_sum)
        else:
            return sum(player_sum)

user_cards = [deal_card(),deal_card()]
computer_cards = [deal_card(),deal_card()]

while not game_end:
    
    

    computer_sum = calculate_score(player_sum=computer_cards)
    user_sum = calculate_score(player_sum=user_cards)

    if user_sum == 0 or computer_sum == 0 or user_sum > 21:
        game_end = True
        
    else:
        a = input("Do you want to draw another card? (y/n): ")
        if a == "y":
            user_cards.append(deal_card())
            
        elif a == "n":
             print("your turn is over")
            
    while computer_sum <= 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(player_sum=computer_cards)
        print(computer_sum)
        game_end = True
        
