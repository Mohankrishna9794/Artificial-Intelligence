def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()
def check_winner(board):
    for row in board + list(zip(*board)) + [[board[i][i] for i in range(3)]] + [[board[i][2 - i] for i in range(3)]]:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    return None
def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]    
    for turn in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {players[turn % 2]}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = players[turn % 2]
            if (winner := check_winner(board)):
                print_board(board)
                print(f"Player {winner} wins!")
                return
        else:
            print("Cell occupied, try again.")
            turn -= 1  # Retry same turn    
    print_board(board)
    print("It's a tie!")
tic_tac_toe()
