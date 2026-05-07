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
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10] # A = 11 to start, if sum > 21, then A becomes 1. ; J = Q = K = 10; Initialized on drawing. Later we'll create a fixed deck
    return random.choice(deck)

def check_21(hand):
    # For every "1" in the hand, we need to replace with different combinations using 1 or 11 and computing the sum.
    # Then take the highest sum that is less than 21 as the FINAL_SUM.

    if sum(hand) > 21:
        return "Bust"
    elif sum(hand) == 21:
        return "Hold"
    elif sum(hand) < 21:
        return "Short"

def round_end_conditions(player_hand, dealer_hand):
    if check_21(player_hand) == "Bust":
        print('Dealer Wins by Default -- Player Bust!\n')
        return 'D'
    elif check_21(dealer_hand) == "Bust":
        print('Player Wins -- Dealer Bust!\n')
        return 'P'
    else:
        # If no busts, compare scores
        final_player_total = sum(player_hand)
        final_dealer_total = sum(dealer_hand)

        print(f"\n>> >> >> >> >> Final Player's Hand = {player_hand}, Final Player Total = {final_player_total} << << << << <<")   
        print(f"\n>> >> >> >> >> Final Dealer's Hand = {dealer_hand}, Final Dealer Total = {final_dealer_total} << << << << <<\n") 

        if final_dealer_total < final_player_total <= 21:
            print('Player Wins!\n')
            return 'P'
        elif final_player_total == final_dealer_total:
            print('Tie!\n')
            return 'T'
        elif final_player_total < final_dealer_total <= 21:
            print('Dealer Wins\n')
            return 'D'
        else:
            print("OOOOOOOOOOOOHHHH MAN, SOMETHING WENT WRONG!\n")
            return 'F'

print(30*'\n' + '++++++++++ Welcome to Blackjack +++++++++++')

def round_of_blackjack():

    dealer_hand = []
    player_hand = []

    # Draw two initial cards for each player and dealer
    for i in range(2):
        player_hand.append(draw())
        dealer_hand.append(draw())

    print(f"Player's Hand = {player_hand}, total = {sum(player_hand)}")
    print(f"Dealer's Hand = [{dealer_hand[0]}, ?]") # Only display one of dealer's cards.

    # Player's Action
    player_stand_or_draw = 0 # Initialized for 1st iter.
    while (player_stand_or_draw != 's') and (check_21(player_hand) != 'Bust'):           # So long as player DOES NOT stand and their hand is NOT a BUST
        if check_21(player_hand) == 'Hold':                                              # If it equals 21, then automatically Hold, and break out of the loop
            print("\nPlayer has 21 ... Move to Dealer\n")
            break

        player_stand_or_draw = 0 # reset stand-draw choice after each iter.
        # Make sure Player chooses ONLY 's' or 'd'.
        while not ( (player_stand_or_draw == 's') or (player_stand_or_draw == 'd') ):    
            player_stand_or_draw = input("\n>>> Player: Stand (s) or Draw (d): ")           # Keep asking them.

        # After determining 's' or 'd' ...
        if player_stand_or_draw == 'd': # draw card
            print('\n>>> Player Draws!\n')
            player_hand.append(draw())

            # This will replace the Ace value of 11 each time the player busts.
            if ( 11 in player_hand ) and ( sum(player_hand) > 21 ): # If there is an 11 in Player's hand and if the sum (after drawing a new card) > 1
                player_hand[player_hand.index(11)] = 1 # replace the value.
                print("Player's Ace Value of 11 is replaced by 1...")
            
            print(f"\nPlayer's Hand = {player_hand}, Total = {sum(player_hand)}, Status = {check_21(player_hand)}\n")        # Print out new hand & total

            if check_21(player_hand) == 'Bust':
                break
        
        elif player_stand_or_draw == 's':                                              # If player stands,
            print('\n>>> Player Stands! Move to Dealer...\n')
            break                                                                      # Break out of loop


    if check_21(player_hand) != 'Bust': # Only run is player is NOT Bust
        # Dealer's Action
        print("\n>>> DEALER'S TURN\n")
        print(f"\n>>> DEALER'S Hand: {dealer_hand}, DEALER'S Total: {sum(dealer_hand)}\n")

        while ( sum(dealer_hand) < 17 ) and ( sum(dealer_hand) < sum(player_hand) ): # and not DEALER_WIN_STATE: # Dealer must draw <= 16 and must hold >= 17
            print('\n>>>Dealer Draws a card\n')
            dealer_hand.append(draw())

            if ( 11 in dealer_hand ) and ( sum(dealer_hand) > 21 ): # If there is an 11 in Player's hand and if the sum (after drawing a new card) > 1
                dealer_hand[dealer_hand.index(11)] = 1 # replace the value.
                print("Dealer's Ace Value of 11 is replaced by 1...")

            print(f"\n>>> DEALER'S Hand: {dealer_hand}, DEALER'S Total: {sum(dealer_hand)}\n")

            if (sum(dealer_hand) > 21):
                break

    # Round end conditions
    return round_end_conditions(player_hand=player_hand, dealer_hand=dealer_hand)


play_blackjack_FLAG = True

while play_blackjack_FLAG:
    num_rounds = input('How many rounds of Blackjack do you want to play? [1]: ') # Create user control incase they enter non-numeric
    if num_rounds == "":
        num_rounds = 1
    else:
        num_rounds = int(num_rounds)

    blackjack_win_dict = {'Player':0, 
                        'Dealer':0}

    for i in range(num_rounds):
        winner = round_of_blackjack()

        if winner == 'P':
            print(f"Player wins round {i+1}" + "\n"*10)
            blackjack_win_dict['Player'] += 1
        elif winner == 'D':
            print(f"Dealer wins round {i+1}" + "\n"*10)
            blackjack_win_dict['Dealer'] += 1
        elif winner == 'T':
            print(f"Player & Dealer BOTH Tie (WIN!) round {i}" + "\n"*10)
            blackjack_win_dict['Player'] += 1
            blackjack_win_dict['Dealer'] += 1
        else:
            print('Something went wrong!')

    #print(f'Blackjack Score: {blackjack_win_dict}')

    if blackjack_win_dict['Player'] > blackjack_win_dict['Dealer']:
        print('Overall winner is PLAYER!' + "\n"*5)
    elif blackjack_win_dict['Player'] < blackjack_win_dict['Dealer']:
        print('Overall winner is DEALER!' + "\n"*5)
    else: 
        print('No Overall Winner' + "\n"*5)

    play_more = input('Would you like to play more? y/[n]')

    if play_more != 'y':
        play_blackjack_FLAG = False
        


