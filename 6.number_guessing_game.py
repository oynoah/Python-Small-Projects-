import random

def guessing_game():
    comp_choice = random.randint(0,100)

    while True:
        user_choice = int(input('Enter your guess: '))
        if user_choice == comp_choice:
            print('Just Right')
            break
        elif user_choice > comp_choice:
            print(f'Too High. The number is {comp_choice}')
        else:
            print(f'Too Low. The number is {comp_choice}')
    print(comp_choice)
guessing_game()
