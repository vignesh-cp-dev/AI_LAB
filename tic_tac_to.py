import random
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, symbol):
    # Winning combinations (Rows, Columns, Diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def check_draw(board):
    return all(space in ['X', 'O'] for space in board)

def tic_tac_toe():
    print("==========================================")
    print("           TIC-TAC-TOE GAME               ")
    print("==========================================")
   
    board = [str(i + 1) for i in range(9)]  # Board indexed 1 to 9
    human = 'X'
    computer = 'O'
    current_turn = human

    print_board(board)

    while True:
        if current_turn == human:
            print("--- Human's Turn (X) ---")
            try:
                move = int(input("Enter position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] in ['X', 'O']:
                    print("Invalid move or position already occupied. Try again.")
                    continue
                board[move] = human
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
        else:
            print("--- Computer's Turn (O) ---")
            # General AI: Choose a random available cell (no standard algorithm used)
            available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
            move = random.choice(available_moves)
            board[move] = computer
            print(f"Computer placed 'O' at position {move + 1}")

        print_board(board)

        # Check Win Condition
        if check_win(board, current_turn):
            if current_turn == human:
                print("Congratulations! You (Human) Won!")
            else:
                print(" Computer Won!")
            break

        # Check Draw Condition
        if check_draw(board):
            print("It's a Draw!")
            break

        # Switch Turns
        current_turn = computer if current_turn == human else human
tic_tac_toe()
