import programs_data.d014_game_data as game_data
import random

def choose_b(choice_a):
    choice_b = random.choice(GAME_DATA_MASTER_LIST) # Selects and fixes choice
    while choice_a == choice_b:
        choice_b = random.choice(GAME_DATA_MASTER_LIST)
    return choice_b

def description_construct(choice_dict_entry):
    return f"{choice_dict_entry['name']} a {choice_dict_entry['description']} from {choice_dict_entry['country']}" #+ f" Followers = {choice_dict_entry['follower_count']}" # TESTING

GAME_DATA_MASTER_LIST = game_data.data # List of dicts 50 entries
# Dict Key struct: 'name', 'follower_count', 'description', 'country' 

print('\n'*10 + '+++++++++++++ Welcome to Higher or Lower! +++++++++++++')
print("In this game, you'll simply select which of two choices has more followers.")

#ready_Q = input('Ready to play? y/[n]')


choice_offer_a = random.choice(GAME_DATA_MASTER_LIST)

player_score = 0
highest_score = 0
play_flag = True
while play_flag:
    choice_offer_b = choose_b(choice_offer_a) # Hypothetically, this could choose the same option as the previous round, then it's a freebie for the player!

    #player_lose_Q = False
    #while not player_lose_Q: # while the player has not lost.

    print(f'\n>> Choice A: {description_construct(choice_offer_a)}')
    print(f'>> Choice B: {description_construct(choice_offer_b)}')

    user_choice = str(input('Which choice (a) or (b) has more followers? ')).lower()
    while user_choice not in ['a', 'b']:
        user_choice = str(input('Which choice (a) or (b) has more followers? ')).lower()

    if user_choice == 'a':
        choice_entry = choice_offer_a
        compare_entry = choice_offer_b
    else:
        choice_entry = choice_offer_b
        compare_entry = choice_offer_a


    if choice_entry['follower_count'] > compare_entry['follower_count']:
        print('Correct!')
        player_score += 1
        print(f"\nCURRENT ROUND SCORE = {player_score}\n")
        choice_offer_a = choice_entry
        continue
    else:
        print('Wrong!')
        play_flag = False
        play_again = input('Play Again? (We keep track of your highest score) y/[n]: ')
        if play_again == 'y':
            if player_score > highest_score: # Check if any new high score
                print('You beat your highest score this round!')
                highest_score = player_score
            play_flag = True
            player_score = 0 # reset for next round
            continue
        else:
            if player_score > highest_score: # Check if any new high score
                print('You beat your highest score this round!')
                highest_score = player_score
            break




print(f'Game Over! Your Current Round score was {player_score}')
print(f'Game Over! Your Highest Score was {highest_score}')
print('\nThanks for playing!')










