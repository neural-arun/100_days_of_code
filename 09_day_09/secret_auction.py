import os
from art import logo
should_continue = True
secret_auction = []
while should_continue:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    print(logo)
    name = input("Enter Your Name: ")
    bid_price = int(input("Enter your bidding price: "))
    name_and_bid = {}
    
    name_and_bid["Name of the bidder"] = name
    name_and_bid["Bidding amount"] = bid_price
    secret_auction.append(name_and_bid)

    clear()
    result = input("is there a next bidder?(yes/no): ")
    if result == "no":
        should_continue = False
        print("Thank you for Bidding.")

highest_bid = 0
for bid in secret_auction:
    if bid["Bidding amount"] > highest_bid:
        highest_bid = bid["Bidding amount"]
        name = bid["Name of the bidder"]
print(f"The highest Bid is {highest_bid} and it goes to Mr. {name}.")