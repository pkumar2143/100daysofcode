# Day 7: Beginner Hangman
import random as rand

def display_word_and_livesleft(guessed_word_array, lives_left):
    lives = ["""
        ------------
            |      |
                   |
                   |
                   |
                   |
                ------""",
             """
        ------------
            |      |
            o      |
                   |
                   |
                   |
                ------""",
             """
        ------------
            |      |
            o      |
            |      |
            |      |
                   |
                ------""",
             """
        ------------
            |      |
            o      |
           /|      |
            |      |
                   |
                ------""",
             """
        ------------
            |      |
            o      |
           /|\     |
            |      |
                   |
                ------""",
             """
        ------------
            |      |
            o      |
           /|\     |
            |      |
           /       |
                ------""",
             """
        ------------
            |      |
            o      |
           /|\     |
            |      |
           / \     |
                ------""",
             ]

    print(lives[6 - lives_left])
    print("Lives left = ", lives_left)
    print(" ".join(guessed_word_array))

    return None


word_list = ["assembly", "bash", "cplusplus", "css", "csharp", "go", "fortran", "go", "html", "java", "javascript",
             "python", "perl", "ruby", "linux", "windows", "macos", "shell", "binary", "mathematica", "matlab",
             "ubuntu", "fedora", "developer", "development", "engineer", "software", "php", "sql", "kotlin", "android",
             "api", "bug", "debug", "algorithm", "kernel", "microsoft", "machine", "turing", "testing", "mysql", "hdmi",
             "compiler", "program", "array", "loops", "oop", "objects", "games", "string", "float", "integer", "double"]

chosen_word = rand.choice(word_list) # Randomly choose a word
guessed_word_array = ["-"]*len(chosen_word) # create a list to keep track of guesses
print("The selected word,", " ".join(guessed_word_array), " has ", len(chosen_word), " letters.")

valid_characters = "abcdefghijklmnopqrstuvwxyz"
lives_left = 6
while lives_left > 0:
    print(" ")
    guessed_letter = input("Guess a letter: ").lower()  # Ask user to guess a letter. Always of type str

    # Make sure letter has not been guessed and that user entry is valid
    if (guessed_letter in guessed_word_array) or (guessed_letter not in valid_characters):
        print("You either already guessed the letter or it is invalid. You lose a life!")
        lives_left -= 1
        display_word_and_livesleft(guessed_word_array, lives_left)
        if lives_left == 0:
            print("XXXXXXXXXX You Lose! XXXXXXXXX")
            print("The word is '", chosen_word, "'")
            break
        continue

    if guessed_letter in chosen_word:
        print("Correct!")
        for i in range(len(chosen_word)):
            if guessed_letter == chosen_word[i]:
                guessed_word_array[i] = guessed_letter
    else:
        print("Wrong!")
        lives_left -= 1


    display_word_and_livesleft(guessed_word_array, lives_left)
    if "".join(guessed_word_array) == chosen_word:
        print(" ------------------ YOU WIN!!! ------------------- ")
        break

    if lives_left == 0:
        print("XXXXXXXXXX You Lose! XXXXXXXXX")
        print("The word is '", chosen_word, "'")



