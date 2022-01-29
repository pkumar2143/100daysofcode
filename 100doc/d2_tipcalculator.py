# Day 2: Tip Calculator

# Greeting
print('Welcome to the Tip Calculator!')

total_bill = float(input("What was the total bill? "))
tip_pct = float(input("What tip percentage would you like to give? (10, 12, or 15)? "))
num_people = int(input("How many people will split the bill? "))

individual_bill = round(total_bill * (1 + 0.01 * tip_pct) / num_people, 2)

print("Each person will pay $", individual_bill)