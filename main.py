from random import choice

def gameStart():
    jokenpo = ['rock', 'scissors', 'papper']

    pc = choice(jokenpo)

    start_match = input('Want play a jokenpo game? (yes/no) ').lower()

    player_score = 0
    pc_score = 0
    tied_game = 0

    while start_match == 'yes':
        print('Rock, scissors, paper?: ')

        player = input('Digit your choice: ').lower()

        while player not in jokenpo:
            player = input('Invalid command, digit again: ')

        if player == pc:
            print(f"Player {player} and PC {pc} it's a draw.")
            tied_game +=1
            start_match = input('Play again ? (yes/no) ')

        elif player == 'rock' and pc == 'scissors':
            print(f'You won: Player {player} smashes Pc {pc}')
            player_score +=1
            start_match = input('Play again ? (yes/no) ')


        elif player == 'scissors' and pc == 'papper':
            print(f'You won: Player {player} cut off PC {pc}')
            player_score +=1
            start_match = input('Play again ? (yes/no) ')


        elif player == 'papper' and pc == 'rock':
            print(f'You won: Player {player} wraps PC {pc}??? ok...')
            player_score +=1
            start_match = input('Play again ? (yes/no) ')


        else:
            print('You Lost! PC detonate you lol')
            pc_score +=1
            start_match = input('Play again ? (yes/no) ')
            
    return result(player_score, pc_score, tied_game)
    

def result(player_score, pc_score, tied_game):  
    print(f'''
    You won: {player_score}
    You lost: {pc_score}
    You tied: {tied_game}
    ''')

if __name__ == '__main__':
    gameStart()