import os

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bids = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder] 
        if bid_amount > highest_bids:
            highest_bids = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bids of ${highest_bids}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your Bids Amount?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
















