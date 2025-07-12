# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from typing import Any

from art import logo
bidding = True
bidders = {}

#function find the higest bidder
def highest_bid():
    #created two varibale to store the updated value
    highest_bidder = 0
    winner = ""
    #looping through the names which is bids within the dictionary bidders
    for bids in bidders:
        # made a varibale to store the amount, from the pull data when accessing through the given name
        bid_amount = bidders[bids]
        #this check if the bid amount is higher then the perivous highest bid, if so it store within it and store the anme of the bidder
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bids
    print(f"the winner is {winner} with {highest_bidder}")
    
    
while bidding:
    print(logo)
    print("Welcome to the secret auction program")
    more_bid = input("Are you ready to bid : type 'y' to bid or type 'n' to stop the bidding ").lower()
    if more_bid == 'y':
        name = input("What is your name?: ")
        print(name)
        price = int(input("what is your bid "))

        if name in bidders:
            print(f"Welcome back, {name}. Adding to your previous bid.")
            bidders[name] += price  # Add to existing bid
        else:
             bidders[name] = price
             print(f" welcome bidders {name}")
    elif more_bid == 'n':
         bidding = False
         print("Thank you bidding will end now")
for bids in bidders:
    print(bids + ": " + bidders[name])
  
highest_bid()
