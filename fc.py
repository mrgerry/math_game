import random
import os 

def main():
    
    game_menu() 

def clear_screen():
    os.system('clear')
    os.system('cls')

def game_menu():
    
    print("Let's learn math!")
    print('')
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("q to quit")
    print('')
    choice = input('Please choose 1, 2, 3 or 4: ').lower()

    while True:
        if choice == ['q','quit']:
            quit()
        elif choice == '':
            print('You did not enter a valid choice.')
            choice = input('Please choose 1, 2, 3 or 4: ')
        if choice == '1':
            add()
        if choice == '2':
            subtract()
        if choice == '3':
            multiply()
        if choice == '4':
            division()
       
# === Ask user if they want to play again or not.
def play_again():       
    
    user_input = input('Do you want to play again y/n ?').lower()

    if user_input == 'y' or user_input == 'yes':
        game_menu()
    else:
        quit()
       
# === Operator Functions ===
def add():
    clear_screen()
    score = 0
    for i in range(5):

            x = random.randint(1, 12)
            y = random.randint(1, 12)
            total = x + y
            
            try:
                print()
                guess = int(input(f'What is {x} + {y}? '))
            except ValueError:
                continue
            
            if guess == total:
                print()
                print(f"That's correct, {x} + {y} = {total}")
                score += 1
            elif guess != total:
                print('Sorry, that is incorrect.')

    print()
    print(f'You gpt {score} out of 5 questions correct.')
    print()
    play_again()
            
def subtract():
    clear_screen()
    score = 0
    for i in range(5):
        
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            total = x - y
            
            try:
                print()
                guess = int(input(f'What is {x} - {y}? '))
            except ValueError:
                continue
            
            if guess == total:
                print()
                print(f"That's correct, {x} + {y} = {total}")
                score += 1
            elif guess != total:
                print('Sorry, that is incorrect.')

    print()
    print(f'You gpt {score} out of 5 questions correct.')
    print()    
    play_again()

def multiply():
    clear_screen()
    score = 0
    for i in range(5):
        
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            total = x * y
            
            try:
                print()
                guess = int(input(f'What is {x} * {y}? '))
            except ValueError:
                continue
            
            if guess == total:
                print()
                print(f"That's correct, {x} * {y} = {total}")
                score += 1
            elif guess != total:
                print('Sorry, that is incorrect.')

    print()
    print(f'You gpt {score} out of 5 questions correct.')
    print()    
    play_again()

    
def division():
    clear_screen()
    score = 0
    for i in range(5):
       
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        total = x // y
        
        try:
            print()
            guess = int(input(f'What is {x} / {y}? '))
        except ValueError:
            continue
        
        if guess == total:
            print()
            print(f"That's correct, {x} / {y} = {total}")
            score += 1
        elif guess != total:
            print('Sorry, that is incorrect.')
                
    print()
    print(f'You gpt {score} out of 5 questions correct.')
    print()    
    play_again()

      
main()