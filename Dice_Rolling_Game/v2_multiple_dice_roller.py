# Multiple Dice Roller

import random

playing = True
count = 0

while True:
    # User Choice
    choice = input("roll the dice? (y/N)").lower()

    # Roll Dice
    if choice == 'y' :
        count += 1

        # Number of Dice 
        num = int(input("Enter the no of dices want to roll"))

        # Generates The Dice Roll
        for i in range(num):
            dice = random.randint(1,6)
            print(dice)
            
     # Exit game       
    elif choice == 'n':
        print('thanks for playing')
        print("number of times dice is rolled",count)
        break
        
    # Invalid input
    else:
        print("Invalid choice")
