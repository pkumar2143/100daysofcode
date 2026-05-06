# Day 4: Random Password Generator
import random as rand
import string

# Lists of all possible characters for the password
numbers = list('0123456789')
uppercase_letters = list(string.ascii_uppercase) # Cheating a bit, hehe >:-)
lowercase_letters = list(string.ascii_lowercase) # Cheating a bit, again, hehe >:-)
symbols = list('!@#$%^&*()')

# Start the program and ask how many chars of each character category the user wants.
print('Hello! Welcome to the Random Password Generator!')
num_uppercase = int(input('How many uppercase letters would you like?: '))
num_lowercase = int(input('How many lowercase letters would you like?: '))
num_numbers = int(input('How many numbers would you like?: '))
num_symbols = int(input('How many symbols would you like?: '))

# List of randomly chosen chars of each character category specified by user.
random_number_list = rand.choices(numbers, k=num_numbers)
random_uppercase_list = rand.choices(uppercase_letters, k=num_uppercase)
random_lowercase_list = rand.choices(lowercase_letters, k=num_lowercase)
random_symbols_list = rand.choices(symbols, k=num_symbols)

# Combine char lists, randomly shuffle the list, and join the characters into a final string
big_character_list = random_number_list + random_uppercase_list + random_lowercase_list + random_symbols_list
rand.shuffle(big_character_list)
final_password = ''.join(big_character_list)

# Print password results.
print('You password is: ', final_password)
print('The total length of your password is:', len(final_password))

#if __name__ == '__main__':
    #print(random_symbols_list)
    #print(random_uppercase_list)
    #print(random_lowercase_list)
    #print(random_number_list)