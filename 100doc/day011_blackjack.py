# Blackjack
# Rules:
#   + Number cards are their own value
#   + Face cards are valued at 10
#   + A = 1 or 11 (depending on total hand)
#   + Two players:
#       ~ Player & Dealer
#   + Both start with 1 card face-up
#   + 2nd card dealt: Player's is revealed (face up); Dealer's is face down.
#   + If Player goes over 21, you LOSE no matter what the dealer has.
#   + If Player hand total = Dealer hand total, result = Draw
#   + If Dealer ends up with hand < 17, they must draw another card
import random

def draw():
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] # A = 1 or 11 ; J = Q = K = 10; Initialized on drawing. Later we'll create a fixed deck
    return random.choice(deck)

def ace_value_replace(hand):
    '''
    Assume there is a 1 in the hand.
    Note: we can have AT MOST one 11 in hand, because if we have more, it's BUST! 
    '''
    if ( 1 in hand ) and ( (21 - sum(hand)) >= 11 ): # If there is a 1 AND the diff between the hand_total and 21 >= 11.
        hand_copy = hand
        hand_copy[hand_copy.index(1)] = 11 # Replace only the first instance of 1 with 11.
        return hand_copy
    else:
        return hand # Original hand.
    

def check_21(hand):
    # For every "1" in the hand, we need to replace with different combinations using 1 or 11 and computing the sum.
    # Then take the highest sum that is less than 21 as the FINAL_SUM.

    if sum(hand) > 21:
        return "Bust"
    elif sum(hand) == 21:
        return "Hold"
    elif sum(hand) < 21:
        return "Short"


# If at ANY time a "1" (Ace) is dealt, then you have to compare two hand lists
# One original
# One replacing the first instance of 1 with 11.

def ace_replace(hand):
    '''
    Assume there is a 1 in the hand.
    Note: we can have AT MOST one 11 in hand, because if we have more, it's BUST! 
    '''
    replaced_hand = hand.copy() # created a shallow copy to not affect original hand.
    replaced_hand[replaced_hand.index(1)] = 11 # replace the first 1 with 11

    return replaced_hand

    


print(30*'\n' + '++++++++++ Welcome to Blackjack +++++++++++')

dealer_hand = []
player_hand = []

# Draw two initial cards for each player and dealer
for i in range(2):
    player_hand.append(draw())
    dealer_hand.append(draw())

######### DEBUGGING ###########
player_hand = [1,1]
###############################

print(f"Player's Hand = {player_hand}, total = {sum(player_hand)}")

if 1 in player_hand:
    alt_hand_sum = sum(player_hand) + 10
    print(f"Alternative Total = {alt_hand_sum}")
    

print(f"Dealer's Hand = [{dealer_hand[0]}, ?]") # Only display one of dealer's cards.

# Player's Action
player_stand_or_draw = 0 # Initialized for 1st iter.
while (player_stand_or_draw != 's') and (check_21(player_hand) != 'Bust'): # So long as player DOES NOT stand and their hand is NOT a BUST
    if check_21(player_hand) == 'Hold': #If it equals 21, then automatically Hold, and break out of the loop
        print("Player has 21 ... Move to Dealer")
        break

    player_stand_or_draw = 0 # reset stand-draw choice after each iter.
    # Make sure Player chooses ONLY 's' or 'd'.
    while not ( (player_stand_or_draw == 's') or (player_stand_or_draw == 'd') ): 
        player_stand_or_draw = input(">>> Player: Stand (s) or Draw (d): ")            # Keep asking them.

    # After determining 's' or 'd' ...
    if player_stand_or_draw == 'd': # draw card
        print('>>> Player Draws!')
        player_hand.append(draw())
        print(f"Player's Hand = {player_hand}, total = {sum(player_hand)}")        # Print out new hand & total

        if 1 in player_hand:
            alt_hand_sum = sum(player_hand) + 10
            print(f"Alternative Total = {alt_hand_sum}")

        print(check_21(player_hand))
        continue
    elif player_stand_or_draw == 's':                                              # If player stands,
        print('>>> Player Stands!')
        print(f">> >> >> >> >> Final Player's Hand = {player_hand}, Final Player Total = {sum(player_hand)} << << << << <<")

        exist_1_BOOL, replaced_hand = ace_sum_checker(player_hand)
        if exist_1_BOOL:
            print(f"Player's Final Hand (REPLACING '1') = {replaced_hand}, Final Player Total (REPLACING '1') = {sum(replaced_hand)}")
            print(check_21(replaced_hand))

        break                                                                      # Break out of loop



#if __name__ == "__main__":
#    list1 = [draw(), draw()]
#    print(list1)
#    print(sum(list1))
