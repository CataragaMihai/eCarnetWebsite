#A game of rock paper scissors 

import random as r

choices: dict[str, str] = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

while True:
    print('What do you play rock(🪨), paper(📄) or scissors(✂️)?')
    player_choice: str = input('Type here: ').strip().lower()

    computer_choice: str = r.choice(tuple(choices))
    if player_choice not in choices:
        print('Choice is not valid!')

    else: 
        print('\nResults: ')
        print('='*30)
        print('You chose: ', player_choice)
        print('='*30)
        print('The computer played: ', computer_choice)
        print('-'*30)

        if player_choice == computer_choice:
            print('It\'s a tie')

        elif player_choice == 'rock' and computer_choice == 'scissors':
            print('You won with rock!')
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You won with scissors!')
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You won with paper!')
        else:
            print('The machine won 🤖')
        print('-'*30 + "\n")
        
    answer: str = input("End the game(yes/no):  ").strip().lower()
        
    if answer == 'yes':
        break
    elif answer == 'no':
        continue
    else: 
        print('Optiune invalida')