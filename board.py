# var definition
player_id = 1
player_win = 0

# function definition
def clear_board:
    row1 = ['-', '-', '-']
    row2 = ['-', '-', '-']
    row3 = ['-', '-', '-']
    
    board = [row1, row2, row3]
    mark = ""

def print_board():
    print(*board, sep = "\n")
    print("")

def check_mark(row, col):
    if board[row][col] != '-':
        return 'false'
    else:
        return 'true'

def place_mark(row, col, player_id):
    #Determine mark style
    if player_id == 1:
        mark = 'X'
    else:
        mark = 'O'
  
    #Determine Placement
    if mark != "":
        board[row][col] = mark

def check_win(player_id):
    #Player 1 Check
    if player_id == 1:
    #Horizontals
        if row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
            player_win = 1
        elif row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
            player_win = 1
        elif row3[0] == 'X' and row3[1] == 'X' and row3[2] == 'X':
            player_win = 1
    #Verticals
        elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X':
            player_win = 1
        elif row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X':
            player_win = 1
        elif row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
            player_win = 1
    #Diagonals
        elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X':
            player_win = 1
        elif row3[0] == 'X' and row2[1] == 'X' and row1[2] == 'X':
            player_win = 1
        else:
            continue

    #Player 2 Check
    if player_id == 2:
    #Horizontals
        if row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
            player_win = 2
        elif row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
            player_win = 2
        elif row3[0] == 'O' and row3[1] == 'O' and row3[2] == 'O':
            player_win = 2
    #Verticals
        elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O':
            player_win = 2
        elif row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O':
            player_win = 2
        elif row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
            player_win = 2
    #Diagonals
        elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O':
            player_win = 2
        elif row3[0] == 'O' and row2[1] == 'O' and row1[2] == 'O':
            player_win = 2
        else:
            continue
    if player_win == 1:
        print("Player 1 Wins!")
    elif player_win == 2:
        print("Player 2 Wins!")
    elif player_win == 3:
        print("It's a draw!")
    else:
        print("No wins yet.")

# tests the function of all functions
def main():
    print("Beginning testing...")
    print("Clearing the board...")
    clear_board()
    
    print("print_board() Test:")
    print_board()
  
    print("Before placing a mark, check_mark for 1, 1 is... ", check_mark(1,1), "\n")

    place_mark(1,1,1)
    print("After placing a mark, check_mark for 1, 1 is... ", check_mark(1,1), "\n")

    print_board()

    print("Adding more markers to the board... \n")
    place_mark(0,0,1)
    place_mark(2,1,1)
    place_mark(2,0,2)
    place_mark(2,2,2)
    place_mark(1,2,2)
    place_mark(0,2,2)

    print_board()
    print("Checking Player 1 Win Status...")
    check_win(1)

    print("Checking Player 2 Win Status...")
    check_win(2)

    print("Test Complete.")

main()