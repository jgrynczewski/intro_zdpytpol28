import random

game = {
    'papier': 1,
    'kamień': 2,
    'nożyce': 3
}


res = input("Podaj wartość ['papier', 'kamień', 'nożyce']: ")
user_choice = game[res]
computer_choice = random.randint(1, 3)
if user_choice == computer_choice:
    print("Remis")
if user_choice == 1:
    if computer_choice == 2:
        print("Wygrałeś")
    elif computer_choice == 3:
        print("Przegrałeś")
if user_choice == 2:
    if computer_choice == 1:
        print("Przegrałeś")
    elif computer_choice == 3:
        print("Wygrałeś")
if user_choice == 3:
    if computer_choice == 1:
        print("Wygrałeś")
    elif computer_choice == 2:
        print("Przegrałeś")
