# Tic-tac-toe game

'''
Basic approach:
Make a 3 * 3 array which contains arrays in them.
Ask for user input from both players
check if the user input is right
assign X and O to the correct values.
Check if there are any rows, columns or diagonals with same input.
show the results.

'''

# Making a 3 * 3 board array

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]


def printing_the_board(board_array):
    for i in range(len(board_array)):
        for j in range(len(board_array[i])):
            if j == 0:
                print("| " + board_array[i][j] + " | ", end="")
            else:
                print(board_array[i][j] + " | ", end="")
        print()

    return " "


# Method that checks if the user input is both a numeric and is in bounds.
def check_input(u_input):
    if not is_num(u_input):
        return False
    u_input = int(u_input)
    if not in_range(u_input):
        return False
    return True


# Method to check if the input is a numeric number.
def is_num(u_input):
    if not u_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


# Method to check if input is in range of 1 to 9.
def in_range(u_input):
    if u_input not in range(1, 10):
        print("This number is out of bounds")
        return False
    else:
        return True


# Method to see if the spots in the array are already taken.
def is_taken(u_input):
    # we should find the row and column of the user_input
    row = u_input // 3
    col = u_input
    if col > 2:
        col = int(col % 3)
    if board[row][col] != "_":
        print("This Value is already taken.")
        return True
    else:
        return False


def assigning_values(board_array, u_input, x_o):
    row = u_input // 3
    col = u_input
    if col > 2:
        col = int(col % 3)
    board_array[row][col] = x_o


# A function that checks rows
def check_rows(board_array, user_sign):
    for row in board_array:
        complete_row = True
        for ele in row:
            if ele.lower() != user_sign.lower():
                complete_row = False
                break
        if complete_row:
            return True

    return False


# A function that checks all the columns.
# For looping over the cols, we need to use the call function first and then use the row function next.
def check_cols(board_array, user_sign):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board_array[row][col] != user_sign:
                complete_col = False
                break

        if complete_col:
            return True
    return False


def check_diagonals(board_array, user_sign):
    if board_array[0][0] == user_sign and board_array[1][1] == user_sign and board_array[2][2] == user_sign:
        return True
    elif board_array[0][2] == user_sign and board_array[1][1] == user_sign and board_array[2][0] == user_sign:
        return True
    return False


def is_win(board_array, user_sign):
    if check_rows(board_array, user_sign) or check_cols(board, user_sign) or check_diagonals(board_array, user_sign):
        return True

    return False


def is_tie(board_array):
    for row in board_array:
        for ele in row:
            if ele == "_":
                return False
    return True


y = 1
sign = "X"
while True:
    print(printing_the_board(board))
    user_input = input(f"{sign}, Please enter a number from 1 to 9 to play or \"q\" to quit: ")
    if user_input.lower() == "q":
        print("Thanks for playing, we look forward to see you next time.")
        break
    if not check_input(user_input):
        print("Please try again")
        continue  # This will make the console to go back to the start of the loop.
    num = int(user_input) - 1
    if is_taken(num):
        print("Please try again")
        continue
    else:
        if y % 2 != 0:

            assigning_values(board, num, sign)

            if is_win(board, sign):
                print(printing_the_board(board))
                print(f"{sign} won Hurray. ")
                break

            if is_tie(board):
                print("This is a tie Match.")
                break

            sign = "O"
            y += 1

        elif y % 2 == 0:

            assigning_values(board, num, sign)

            if is_win(board, sign):
                print(printing_the_board(board))
                print(f"{sign} won Hurray. ")
                break

            if is_tie(board):
                print("This is a tie Match.")
                break

            sign = "X"
            y += 1

print("Game Over")

