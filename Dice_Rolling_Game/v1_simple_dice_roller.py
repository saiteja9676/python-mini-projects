# Dice Rolling Game
# Rolls two dice repeatedly until the user decides to quit

import random

playing = True

while playing:
    # User choice
    choice = input('Roll the Dice (y/n): ').lower()

    # Roll dice
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'{die1, die2}')

    # Exit game
    elif choice == 'n':
        print('Thank you')
        break

    # Invalid input
    else:
        print('Invalid choice')