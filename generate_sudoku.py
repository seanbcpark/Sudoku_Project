import random
import copy

def generate_sudoku():
    board = initialize_board()
    solve_sudoku(board)
    puzzle = copy.deepcopy(board)
    attempts = 30
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = puzzle[row][col]
        puzzle[row][col] = 0
        board_copy = copy.deepcopy(puzzle)
        if not solve_sudoku(board_copy):
            puzzle[row][col] = backup
        attempts -= 1
    return puzzle