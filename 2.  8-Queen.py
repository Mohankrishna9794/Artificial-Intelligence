def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    # If all queens are placed, return True
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place this queen in board[i][col]

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack if placing queen doesn't lead to a solution

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    # Print the solution
    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

# Example usage
n = 8  # Number of queens
solve_n_queens(n)
