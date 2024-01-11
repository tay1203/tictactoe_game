import random
import os

def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("TicTacToe is a two-player game where the")
    print("objective is to get three of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("3x3 grid. The first player to get three")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list.
    :return: The user's input, string.
    """

    # Initialise a variable and set it to True
    not_valid = True
    # Keep asking the user to input if the invalid input is received
    while not_valid:
        # get the input from user
        option = input(prompt)
        # if invalid input is received, print the statement and continue asking for the input
        if not option in valid_inputs:
            print("Invalid input, please try again.")
        # if valid input is received, break the loop and return the user's input
        else:
            not_valid = False
            return option


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """

    # Initialise the variables
    list_2D = []
    row = 3
    column = 3
    # create row for the 2D list
    for x in range(0, row):
        # create a list inside the list
        list_2D.append([])
        # create column for the 2D list
        for y in range(0, column):
            list_2D[x].append([])
            # set the default value to 0
            list_2D[x][y] = 0

    return list_2D


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
        
    print("========== Tic Tac Toe =========")
    print("Player 1: X       Player 2: O\n")
    print("    1   2   3")
    print("   --- --- ---")

    i = 0

    for row in board:
        i += 1
        print(f"{i} |",end="")
        for cell in row:
            if cell == 0:
                print("   |",end="") # 0 for empty cell
            elif cell == 1:
                print(" X |",end="") # fill the cell with players' token
            elif cell == 2:
                print(" O |",end="")
        print("\n   --- --- ---")
    print("=============================")


def drop_piece(board, player, row, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Drop the token of the player into the column 
    # Start with any place in the matrix
    row = row - 1
    column = column - 1

    if board[row][column] == 0:
        board[row][column] = player
        state = True  # the chosen play is succeed
    else:
        state = False # the piece cannot be dropped

    # return the output 
    return state



def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :param player: The player dropping the piece, int.
    :param board: The game board, 2D list of 3x3 dimensions. 
    :return: Column that the piece was dropped into, int.
    """
    # Initialise the variable
    check = False
    while not check:
        try:
            # Prompt the player to enter the choice of column
            acceptable_values = ["1", "2", "3"]
            prompt_statement_row = "Player {}, please enter the row you would like to drop your piece into: ".format(player)
            prompt_statement_col = "Player {}, please enter the column you would like to drop your piece into: ".format(player)
            row = validate_input(prompt_statement_row,acceptable_values)
            row = int(str(row))
            column = validate_input(prompt_statement_col,acceptable_values)
            column = int(str(column))

            # check whether the selected column is full 
            check = drop_piece(board,player,row, column)
            # If the chosen play is successful  
            if (check == True):
                # return the chosen box as list
                return [row, column]
            # If the chosen box is full
            else: 
                print("The box is full, please try again.")
        except EOFError:
            check = True


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 3 rows x 3 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Initialise the state of game as an empty string
    state = ""

    # Horizontal Checker
    # indicate player 1 or 2
    for i in range(1,3):
        # row
        for r in range(0,3):
            # column
            c = 2
            if board[r][c] == board[r][c-1] == board[r][c-2] == i:
                # indicate the winner
                state = i
    # Vertical Checker
    # indiacte player 1 or 2
    for i in range(1,3):
        # column
        for c in range(0,3):
            # row
            r = 2
            if board[r][c] == board[r-1][c] == board[r-2][c]  == i:
                # indicate the winner
                state = i
    # Diagonal Checker
    # indiacte player 1 or 2
    for i in range(1,3):
        r = 0
        c = 0
        if (board[r][c] == board[r+1][c+1] ==board[r+2][c+2] == i) or \
            (board[r+2][c] == board[r+1][c+1] == board[r][c+2]== i):
            # indicate the winner
            state = i
    # Check for available space
    if state == "":
        for r in range(0,3):
            for c in range(0,3):
                if state == "":
                    # when the game is over, the board is full
                    if board[r][c] != 0:
                        state = ""
                    # the game is not over
                    else:
                        state = 0
    # The game is over, it is a draw            
    if state == "":
        state = 3
    # return the state of the game (0,1,2,3)
    return state


def local_2_player_game():
    """
    Runs a local 2 player game of Tic Tac Toe.

    :return: None
    """
    # Initialise the variables
    finish = False
    player = 0
    board = create_board()
    while finish == False:
        clear_screen()
        print_board(board)
        # first game
        if (player == 0):
            # new game starts with player 1
            player = 1
            result = execute_player_turn(player,board)
            row = result[0]
            column = result[1]
        elif (player == 1):
            print(f"Player {player} dropped a piece into {row} x {column}")
            # update the player variable, the next turn
            player = 2
            result = execute_player_turn(player,board)
            row = result[0]
            column = result[1]
        elif (player == 2):
            print(f"Player {player} dropped a piece into {row} x {column}")
            # update the player variable, the next turn
            player = 1
            result = execute_player_turn(player,board)
            row = result[0]
            column = result[1]

        # check the state of the on-going game
        if(end_of_game(board) == 0):
            finish = False
        elif(end_of_game(board) == 1):
            clear_screen()
            print_board(board)
            print("Congratulations! The winner is Player 1")
            finish = True
        elif(end_of_game(board) == 2):
            clear_screen()
            print_board(board)
            print("Congratulations! The winner is Player 2")
            finish = True
        else:
            clear_screen()
            print_board(board)
            print("It is a draw......")
            finish = True

# Task 8    
def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """

    while True:
    # calling clear_screen() to clear the console before displaying a menu screen
        clear_screen()
        try:
            # printing for the header of the main menu
            for i in range(15):
                # end="" is used to print in the same line
                print("=",end="")
            print(" Main Menu ",end="")
            for j in range(15):
                print("=",end="")
            # printing for the content of the main menu
            print("\nWelcome to Tic Tac Toe!")
            print("1. View Rules")
            print("2. Play a local 2 player game")
            print("3. Play a game against the computer")
            print("4. Exit")
            # printing for the footer of the main menu
            for k in range(41):
                print("=",end="")
            print(" ")
            # prompt the user the select an option
            choose = int(input("Please choose an option to proceed: "))
            # after printing rules, prompt user that they can go back to main menu by entering b
            if (choose == 1):
                print_rules()
                invalid = True
                while invalid:
                    back = input("Enter b to back to the main menu: ")
                    if (back == "b"):
                        invalid = False
                    else:
                        print("Invalid input")
            elif (choose == 2):
                local_2_player_game()
                invalid = True
                while invalid:
                    back = input("Enter b to back to the main menu: ")
                    if (back == "b"):
                        invalid = False
                    else:
                        print("Invalid input")
            # elif (choose == 3):
            #     game_against_cpu() 

            elif (choose == 4):
                print("Exiting...")
                break
            else:
                print("Please enter a valid option")

        except ValueError:
            print("Only options 1,2,3,4 can be accepted")

        
if __name__ == "__main__":
	main()