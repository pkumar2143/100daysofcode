alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, en_or_decrypt):
        # Direction of shift (depends on whether encrypting or decrypting)
        if en_or_decrypt == "e":
            factor = 1
        elif en_or_decrypt == "d":
            factor = -1
        else:
            factor = 0
            print("Invalid entry for 'encrypt' or 'decrypt'. Returning original text.")
        
        final_text = ""
        for letter in original_text:
            if letter not in alphabet:
                final_text += letter
            else:
                shifted_position = (alphabet.index(letter) + shift_amount*factor) % len(alphabet)
                final_text += alphabet[shifted_position]
        print(f"Final text = {final_text}")
        return final_text

restart_program = 'y'

while restart_program == 'y':
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text      = input("Type your message:\n").lower()
    shift     = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, en_or_decrypt=direction)
    
    restart_program = input("Type y/[n] if you want to go again:".lower())
    
    if restart_program == 'n' or restart_program == '':
        print("Thanks for using the Caesar cipher! Goodbye!")

