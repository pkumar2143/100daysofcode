# Day 3: Trasure Island Adventure
# Flow chart: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('Welcome to Trasure Island \nYour mission is to find the tresure!')

left_or_right = input('Do you want to go "left" or "right"? ').lower()
if left_or_right != 'left':
    print('Fall into hole! Game over!')
else:
    swim_or_wait = input('Do you want to swim or wait? ').lower()
    if swim_or_wait != 'wait':
        print('Attacked by trout! Game over!')
    else:
        red_blue_or_yellow = input('Choose a door: red, blue or yellow: ').lower()
        if red_blue_or_yellow == 'red':
            print('Burned by fire! Game Over!')
        elif red_blue_or_yellow == 'blue':
            print('Eaten by beasts! Game Over!')
        elif red_blue_or_yellow == 'yellow':
            print('You found the treasure! You win!')
        else:
            print('Game Over')



