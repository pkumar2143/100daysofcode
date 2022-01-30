# Day 4: Play Rock, Paper, Scissors with the computer
import random as rand
# Rock Paper Scissors ASCII Art

# Rock
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art_list = [rock_art, paper_art, scissor_art]

def rps_round():
    # Welcome
    try:
        user_rps = int(input("Ready to play RPS!\nEnter 0 for rock, 1 for paper, 2 for scissors: "))
    except (ValueError, BaseException):
        return None


    computer_rps = rand.randint(0, 2)
    rps_list = ['Rock', 'Paper', 'Scissors']

    user_wins = False
    computer_wins = False
    # Invalid entries end program
    if user_rps not in [0, 1, 2]:
        print('Invalid!')
        return None

    if user_rps == 0 and computer_rps == 2:
        print(f'You chose {rps_list[user_rps]} \n', art_list[user_rps])
        print(f'Computer chose {rps_list[computer_rps]}\n',art_list[computer_rps])
        print('You win!')
        user_wins = True
    elif user_rps == 2 and computer_rps == 0:
        print(f'You chose {rps_list[user_rps]} \n', art_list[user_rps])
        print(f'Computer chose {rps_list[computer_rps]}\n', art_list[computer_rps])
        print('You lose!')
        user_wins = False
    elif user_rps < computer_rps:
        print(f'You chose {rps_list[user_rps]} \n', art_list[user_rps])
        print(f'Computer chose {rps_list[computer_rps]}\n', art_list[computer_rps])
        print('You lose!')
        user_wins = False
    elif user_rps > computer_rps:
        print(f'You chose {rps_list[user_rps]} \n', art_list[user_rps])
        print(f'Computer chose {rps_list[computer_rps]}\n', art_list[computer_rps])
        print('You win!')
        user_wins = True
    elif user_rps == computer_rps:
        print(f'You both chose {rps_list[user_rps]}\n',art_list[user_rps])
        print('Draw!')
        return None

    return user_wins

def multi_rps_rounds():
    try:
        num_rounds = int(input('Number of rounds desired? '))
    except (ValueError, BaseException):
        return print('Make sure your entry is a number. Start the program again.')

    if num_rounds <= 1:
        num_games_to_win = 1
    else:
        num_games_to_win = num_rounds // 2 + 1

    user_win_count = 0
    computer_win_count = 0

    while user_win_count < num_games_to_win and computer_win_count < num_games_to_win:
        user_win_lose = rps_round()
        if user_win_lose == True:
            user_win_count += 1
        elif user_win_lose == False:
            computer_win_count += 1
        elif user_win_lose == None:
            continue

    print('User wins = ', user_win_count, 'Computer wins =', computer_win_count)

    if user_win_count > computer_win_count:
        print('You WIN Overall!')
    else:
        print('You lose overall')

if __name__ == '__main__':
    multi_rps_rounds()


