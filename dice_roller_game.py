"""
Dice Roller Game 🎲
-------------------
A fun command-line game to roll 1 or 2 dice with random faces.

Features:
- Choose to roll 1 or 2 dice
- Dice faces displayed as Unicode emojis (⚀ ⚁ ⚂ ⚃ ⚄ ⚅)
- Input validation and friendly prompts
- Option to play again after each roll
- Uses built-in modules: random, time
"""


import random
import time


def dice_roller():
    """
    Dice Roller Game 🎲
    - Roll 1 or 2 dice with random faces
    - Input validation
    - Option to play again
    """

#Data
    dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

#welcome message
    print("-" * 40)
    print("\nWelcome to Dice Roller Game 🎲 ")
    print("\n"+ "-" * 40)

#outer loop
    while True:

#Input Validation
        while True:
            try:
                choice = int(input("Want to roll 1 or 2 dice: "))
                if choice == 1 or choice == 2:
                    break
                print("Please enter a number between 1 and 2 ")
            except ValueError:
                print("Invalid number...")

#logic
        if choice == 1:
            print("You rolled...")
            time.sleep(1)
            print(f"      {random.choice(dice_faces)}")
        elif choice == 2:
            print("You rolled...")
            time.sleep(1)
            print(f"      {random.choice(dice_faces)}  {random.choice(dice_faces)}")

#play again
        while True:
            print("-" * 40)
            play_again = input("Wanna play again yes/no : ").lower()

            if play_again in ["yes" , "no"]:
                break
            print("Invalid choice...Type yes/no")

        if play_again == "no":
            print("Thanks for playing 😀")
            break
        else:
            print("-" * 40)
            print("\nStarting a new game! 🎲")
            print("\n" + "-" * 40)
            time.sleep(1)
            continue

#calling function
if __name__ == "__main__":
    dice_roller()