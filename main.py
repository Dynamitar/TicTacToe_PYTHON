import random

def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    # WIN TIC TAC TOE?
    # ALL ROWS, and check to see if they all share the same marker?
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            # ALL COLS
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            # 2 diagonals
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


def choose_first():
    flip_number = random.randint(0,1)

    if flip_number == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    # BOARD IS FULL IF RETURN TRUE
    return True


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1 - 9)'))

    return position


def replay():
    replay = input('Play again? Enter Yes or No')
    if replay == 'Yes':
        return True
    else:
        return False


if __name__ == '__main__':

    # test_board = ['#', 'O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O']

    print('TIC TAC TOE')

    while True:
        # Play the game
        the_board = [' ']*10
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(turn + ' will go first!')

        play_game = input('Ready to play? y or n?').lower()

        if play_game == 'y':
            game_on = True
        else:
            game_on = False


        # GAME PLAY
        while game_on:

            if turn == 'Player 1':

                # show the board
                display_board(the_board)
                # choose the position
                position = player_choice(the_board)
                # place the marker on the position
                place_marker(the_board,player1_marker,position)
                # check if there is winner
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('PLAYER 1 HAS WON!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('DRAW GAME!!!')
                        game_on = False
                    else:
                        turn = 'Player 2'

            else:

                # show the board
                display_board(the_board)
                # choose the position
                position = player_choice(the_board)
                # place the marker on the position
                place_marker(the_board, player2_marker, position)
                # check if there is winner
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('PLAYER 2 HAS WON!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('DRAW GAME!!!')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            break

