basic_board_layout = """"

+-------+-------+-------+
|       |       |       |
|   a   |   b   |   c   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   d   |   e   |   f   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   g   |   h   |   i   |
|       |       |       |
+-------+-------+-------+ 
"""


# The function accepts one parameter containing the board's current status
# and prints it out to the console.
def display_board(board):
    return print(
        "+-------+-------+-------+\n" +
        "|       |       |       |\n" +
        "|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |\n" +
        "|       |       |       |\n" +
        "+-------+-------+-------+\n" +
        "|       |       |       |\n" +
        "|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |\n" +
        "|       |       |       |\n" +
        "+-------+-------+-------+\n" +
        "|       |       |       |\n" +
        "|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |\n" +
        "|       |       |       |\n" +
        "+-------+-------+-------+"

    )


# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.
def enter_move(board):
    # I want code that asks for a user input, the checks the board to see if the space is free
    # if it is free, update the list by
    ok = False
    um_row = None
    um_col = None
    while not ok:
        user_move = input("Enter your move: ")
        ok = len(user_move) == 1 and user_move >= '1' and user_move <= '9'
        if not ok:
            print("Please input an integer move between 1 and 9")
            continue
        user_move = int(user_move) - 1
        um_row = user_move // 3
        um_col = user_move % 3
        check_spot = board[um_row][um_col]
        ok = check_spot not in ['O', 'X']
        if not ok:
            if check_spot == 'O':
                print("You already played this move. Try a different move.")
            else:
                print("Your opponent already played this move. Try a different move.")
            continue
    board[um_row][um_col] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares_list = []
    for rows in range(3):
        for columns in range(3):
            if board[rows][columns] not in ['O', 'X']:
                free_squares_list.append((rows, columns))
    return free_squares_list


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # diagonals
    if sign == 'X':
        who = 'computer'
    elif sign == 'O':
        who = 'player'
    else:
        who = None
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return who
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return who
    # columns
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return who
    # rows
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return who
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import randrange
    free_moves = make_list_of_free_fields(board)
    moves_left = len(free_moves)
    if moves_left > 0:
        rando_move = randrange(moves_left)
        row, col = free_moves[rando_move]
        board[row][col] = 'X'


playing_board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
# start game display board, (check if there is a winner)
# have player enter a move, display board (check if there is a winner)
# have computer enter a move, display board (check if there iw a winner

free = make_list_of_free_fields(playing_board)
display_board(playing_board)
moves_avail = len(free)
while moves_avail > 0:
    enter_move(playing_board)
    moves_avail = moves_avail - 1
    display_board(playing_board)
    if victory_for(playing_board, 'O') == 'player':
        break
    draw_move(playing_board)
    moves_avail = moves_avail - 1
    display_board(playing_board)
    if victory_for(playing_board, 'X') == 'computer':
        break


if victory_for(playing_board, 'X') == 'computer':
    print("The Computer won.")

elif victory_for(playing_board, 'O') == 'player':
    print("You won.")

else:
    print("Tie.")
