alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
text      = input("Type your message:\n").lower()
shift     = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    # Create an empty list the size of the "original text"
    empty_list = [0]*len(original_text)
    
    # Find the indices of each of the letter and replace in the respective empty list elements
    # Add 'shift_amount' to each index
    # Replace the shifted indices by their respective alphabet letter
    for i in range(len(original_text)):
        if original_text[i] == " ":
            empty_list[i] = " "
        else:
            empty_list[i] = (alphabet_list.index(original_text[i]) + shift_amount) % len(alphabet_list)
            empty_list[i] = alphabet_list[empty_list[i]]
    # Join & return list elements
    final_message = ''.join(empty_list)
    print(final_message)
    return final_message

if direction == 'e': 
    encrypt(text, shift)


