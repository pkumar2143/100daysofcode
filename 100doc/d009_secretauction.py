# Secret Auction

# Start program
bid_dict = {} # initialize bid dict
other_user_Q = 'y' # first user initialized

bidder_id = 1
print('Welcome to the Silent Auction!')

while other_user_Q == 'y':
    print('\n'* 100) # clear console (artificially)

    bid_name = str(input('What is bidder #' + str(bidder_id) + "'s name?: "))     # Ask for bidder's name (user can enter numeric, too)
    
    try:
        bid_price = float(input('What is bidder #' + str(bidder_id) + "'s price?: ")) # Ask for bidder's price
    except ValueError as e: # if user enters a non-numeric bid
        continue            # restart the loop
    
    if bid_name not in bid_dict: # Check if bidder name is already in the dict.
        bid_dict[bid_name] = bid_price  # Add name, price to dict
    else:
        #print('The same bidder name cannot be entered!') # To prevent any changes to bids. Though this will print in the next line not the line before the loop restarts.
        acknowledge = str(input("\nTo prevent alterations of bids, the same name cannot be used! Acknowledge [y]:")) # only for user reading
        continue # restart the loop

    other_user_Q = input('Are there any other bidders? (y/[n]):') # Ask if any more bidders

    if other_user_Q == "":          # if user just presses enter.
        other_user_Q = 'n'              # default: no other users
    elif other_user_Q == "y":       # if user enters 'y'
        bidder_id += 1                  # increase bidder count

# Find the highest bidder (can also turn into a function)
highest_bid_price = 0                           # initialize highest bid price to 0 to compare as we loop through the dict
highest_bid_user = ""                           # initialize highest bidder name string.
for bidder in bid_dict:                         # loop through bidder names
    current_bid_price = bid_dict[bidder]        # the current iteration's price
    if current_bid_price > highest_bid_price:   # compare the highest
        highest_bid_price = current_bid_price   # if the current > highest, reset highest
        highest_bid_user = bidder               # set the new bidder name string.

print('The Winner of the Silent Auction is:', highest_bid_user, ', with a price of', highest_bid_price)


