
# Create functions for all operations +,-,*,/
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    '''Subtracts n2 FROM n1'''
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    '''Divide n1 BY n2'''
    return n1 / n2

def compute(n1, op, n2):
    '''Implements correct operation on n1 & n2'''
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        print('Something went wrong!')
        return None

# If only one of these conditions for the initial while, then entire calculator stops. 
# Want the first calc to go through, and then re-initialize properly with either user entry OR the previous result,
# which depends on whether the user wants a new calculation or continue
new_calc_Q = True # Very first calculation initialized
continue_Q = True 

while new_calc_Q or continue_Q:
    if new_calc_Q == True:
        num1 = float(input("Enter your first number: ")) # Ask user for 1st number, initially
    else:
        num1 = result # Condition only assessed after first iteration.

    op = 0 # controlling user behavior to only enter a legitimate operation, op needs resetting upon continuing OR new calc
    op_entry_counter = 0
    op_entry_FLAG = False
    legit_operation = False # initialize legit_operation Boolean
    while not ( legit_operation ) :
        if op_entry_counter == 5: # Don't want this to run forever
            op_entry_FLAG = True
            break # Break out of THIS while loop
        op = str(input('Select your operation: \n + \n - \n * \n / \n Your operation: '))    # Ask user for operation
        legit_operation = ( op == '+' ) or ( op == '-' ) or ( op == '*' ) or ( op == '/' ) # reset to user's entry
        op_entry_counter += 1
    
    if op_entry_FLAG:
        print('You keep entering bad operations! Thank you for using our calculator!')
        break # Stop calculator


    num2 = float(input("Enter your second number: "))                # Ask user for 2nd number

    # Check operation and input numbers into respective function; produce result
    result = compute(num1, op, num2)
    print(f"Result = {result}")

    # Feel like I can clean this control up a bit more...
    continue_or_new = input('Type "y" to continue calculating with result. Type "n" for a new calculation [DEFAULT]. Type "c" to exit calculator. \nYour entry: ')
    if continue_or_new == "y":
        new_calc_Q = False
        continue_Q = True
        continue
    elif ( continue_or_new == "n" ) or ( continue_or_new == "" ): # default to new calculation
        new_calc_Q = True
        continue_Q = False
        continue
    elif continue_or_new == "c":
        print("Thanks for using our calculator. Goodbye!" + "\n"*100)
        break



# Prompt: Type "y" to continue calculating with result. 
# Assign first_number to result
# Repeat process from asking user for operation thru running the prompt (run prompt as first step)

# Type "n" to start new calculation

