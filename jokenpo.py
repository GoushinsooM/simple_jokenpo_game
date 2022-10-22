from random import randint

jokenpo_computer = ['scissors', 'rock', 'paper']

pc_choice = randint(0, 2)

pc = jokenpo_computer[pc_choice]
player = False

while player == False:
    print('Rock, paper or scissors?: ')
    player_choice = str(input()).lower()

    if player_choice == pc:
        print(f"Player {player_choice} and PC {pc} it's a draw.")
        player = True
      
    #Player win condition
    elif player_choice == 'scissors' and pc == 'paper':
        print(f'You won: Player {player_choice} cut off PC {pc}')
        player = True

    elif player_choice == 'rock' and pc == 'scissors':
        print(f'You won: Player {player_choice} smashes Pc {pc}')
        player = True
    elif player_choice == 'paper' and pc == 'rock':
        print(f'You won: Player {player_choice} wraps PC {pc}??? ok...')
        player = True

    #Pc win condition
    elif pc == 'scissors' and player_choice == 'paper':
        print(f'You lose: PC {pc} cut off Player {player_choice}')
        player = True

    elif pc == 'rock' and player_choice == 'scissors':
        print(f'You lose: PC {pc} smashes Player {player_choice}')
        player = True

    elif pc == 'paper' and player_choice == 'rock':
        print(f'You lose: PC {pc} wraps Player {player_choice}??? ok...')
        player = True
      
    else:
        print(f'{player_choice} is an invalid command, try again')
        pc