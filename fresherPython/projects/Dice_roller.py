import Dice
import time


while True:
    print()
    choice = input('Do you want to roll the dice (yes/no):')
    if choice == 'yes':
        print(f'you got {Dice.roll()}')
    elif choice == 'no':
        print('then quiting...')
        time.sleep(1)
        break
    else:
        print('You have tuped something non-sensible.')