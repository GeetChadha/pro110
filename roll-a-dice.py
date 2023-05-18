import random

response = "y"

while response == "y":
    dice_value = random.randint(1, 6)

    if dice_value == 1:
        print("---------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("---------")
    elif dice_value == 2:
        print("---------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("---------")
    elif dice_value == 3:
        print("---------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("---------")
    elif dice_value == 4:
        print("---------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("---------")
    elif dice_value == 5:
        print("---------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("---------")
    elif dice_value == 6:
        print("---------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("---------")

    response = input("Roll the dice again? (y/n): ")

    if response != "y":
        print("Thank you for playing. Goodbye!")






