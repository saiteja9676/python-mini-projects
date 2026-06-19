# Multiple Dice Roller with Sum


import random

playing = True
count = 0
sum_of_dice = 0

while True:
    # User Choice
    choice = input("roll the dice? (y/N)").lower()

    # Roll Dice
    if choice == 'y' :
        count += 1
        
        # Number of Dice 
        num = int(input("Enter the no of dices want to roll"))
        
        # Check Valid Number
        if num <= 0:
            print("Invalid Number")
            num = int(input("Enter the no of dices want to roll"))
        
        # Generates The Dice Roll
        for i in range(num):
            dice = random.randint(1,6)
            print(f' Dice {i+1}: {dice} ')
            sum_of_dice += dice
        print(f"Sum of dice = {sum_of_dice} ")
            
            
    # Exit game   
    elif choice == 'n':
        print('Thanks for playing')
        print(f"You have played {count} times")
        break

     # Invalid choice   
    else:
        print("Invalid choice")
