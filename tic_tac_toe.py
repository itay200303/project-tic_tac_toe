def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],  # a 3x3 empty board
        'turn': 'X',  # X starts first
        'counter': 1   # keeps track of the number of turns played
    }

def draw_board(game):
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()

def input_square(game, x_or_o):
    while True:
        try:
            position = input(f'Enter location for {x_or_o} (row,col): ')
            row, col = map(int, position.split(','))  # Parse input as row,col
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a location in the range (0,0) to (2,2).")
            elif game['board'][row][col] != '_':
                print("Cell already occupied. Choose a different cell.")
            else:
                return row, col
        except ValueError:
            print("Invalid input format. Please use row,col (e.g., 1,1)")

def check_win(game, x_o: str) -> bool:
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if all([game['board'][i][j] == x_o for j in range(3)]) or \
           all([game['board'][j][i] == x_o for j in range(3)]):
            return True
    # Check diagonals
    if game['board'][0][0] == game['board'][1][1] == game['board'][2][2] == x_o or \
       game['board'][0][2] == game['board'][1][1] == game['board'][2][0] == x_o:
        return True
    return False

def check_tie(game) -> bool:
    return game['counter'] >= 9

def play_x_o():
    # Initialize the game
    my_game = create_game()

    while True:
        # X player's turn
        draw_board(my_game)
        x_row, x_col = input_square(my_game, 'X')
        my_game['board'][x_row][x_col] = 'X'
        my_game['counter'] += 1

        # Check if X wins
        if check_win(my_game, 'X'):
            draw_board(my_game)
            print("Player X wins!")
            break

        # Check for tie
        if check_tie(my_game):
            draw_board(my_game)
            print("It's a tie!")
            break

        # O player's turn
        draw_board(my_game)
        o_row, o_col = input_square(my_game, 'O')
        my_game['board'][o_row][o_col] = 'O'
        my_game['counter'] += 1

        # Check if O wins
        if check_win(my_game, 'O'):
            draw_board(my_game)
            print("Player O wins!")
            break

        # Check for tie
        if check_tie(my_game):
            draw_board(my_game)
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_x_o()


# X O X
# O X O
# X O X

# X _ _
# _ O _
# _ _ _



# counter = 1
    # prepare_board
    # while board_is_not_full and there_is_no_win:
    #   X player, play
    #   input location - valid: 1. range 1-3/1-3 2. free cell
    #   counter += 1
    #   put X in the board
    #   draw the board
    #   check if won ?
    #      check each row X
    #      check each column X
    #      check 2 diagonal X
    #   board is full (counter == 9), tie
    #   O player, play
    #   input location - valid: 1. range 1-3/1-3 2. free cell
    #   counter += 1
    #   put O in the board
    #   board is full (counter == 9), tie
    #   draw the board
    #   check if won ?
    #      check each row O
    #      check each column O
    #      check 2 diagonal O

# X O X
# O X O
# X O X

# X _ _
# _ O _
# _ _ _