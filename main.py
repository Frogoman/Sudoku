# 9x9 array of 0s
# 0s are empty cells
# 1-9 are filled cells


# Check if the number is valid in the row
def is_valid_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    return True

# Check if the number is valid in the column
def is_valid_col(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True

# Check if the number is valid in the 3x3 subgrid
def is_valid_subgrid(board, row, col, num):
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# If the number is valid, fill the cell
def is_valid(board, row, col, num):
    return is_valid_row(board, row, num) and is_valid_col(board, col, num) and is_valid_subgrid(board, row, col, num)

# If the number is not valid, backtrack
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Repeat until the puzzle is solved
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Print the solved puzzle
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def main():
    board = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 1, 6, 9, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 1, 8],
        [0, 0, 0, 8, 4, 6, 5, 0, 0],
        [5, 0, 1, 0, 0, 0, 5, 6, 4],
        [8, 0, 6, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 1, 0, 5],
        [6, 0, 0, 3, 1, 0, 0, 4, 0],
        [1, 2, 0, 0, 9, 0, 6, 7, 3]
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
