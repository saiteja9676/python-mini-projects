# Dice Roller With History


import random

playing = True
counter = 0
all_rolls = {}


while playing:
    # User choice
    choice = input('Roll the Dice (y/n): ').lower()
    
    # Roll dice
    if choice == 'y':
        counter += 1

        # Number of dice
        num = int(input('Enter the no fo dice want to roll: '))

        # Store current roll
        rolls = []

        # Check valid number
        if num <= 0:
            print('Invalid number')
            num = int(input('Enter the no fo dice want to roll: '))
            
        # Generate dice rolls
        for i in range(num):
            dice = random.randint(1,6)
            rolls.append(dice)

        # Save roll history
        all_rolls[f"Roll{counter}"] = rolls.copy()

        # Display current roll
        print(f'Roll{counter} -> {all_rolls[f"Roll{counter}"]}')
        
    # Exit game 
    elif choice == 'n':
        print(f'You have played {counter} times')

        # Display Roll History
        for roll_name, values in all_rolls.items():
            print(f"{roll_name} -> {values}")

        print("\nThank you for playing")
        break
        
    # Invalid Choice   
    else:
        print('Invalid choice')