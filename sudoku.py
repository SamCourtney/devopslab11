def is_valid(board, row, col, num):
    # Check if the number is valid in the row, column, and subgrid.
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
        if board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:
            return False
    return True

def solve_sudoku(board):
    # Backtracking algorithm to solve Sudoku.
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return board
                        board[row][col] = 0
                return False
    return board

def sudoku_solver(board):
    if solve_sudoku(board):
        return board
    else:
        return None

def validate_board(board):
    if not isinstance(board, list) or len(board) != 9:
        raise ValueError("Invalid board: Must be a 9x9 grid.")
    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            raise ValueError("Invalid board: Each row must have 9 elements.")
    return True

def sudoku_solver(board):
    validate_board(board)
    if solve_sudoku(board):
        return board
    else:
        return None
