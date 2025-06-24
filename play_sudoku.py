def play_sudoku():
    puzzle = generate_sudoku()
    while True:
        print_board(puzzle)
        try:
            row = int(input("행 (0-8): "))
            col = int(input("열 (0-8): "))
            num = int(input("숫자 (1-9): "))
            if puzzle[row][col] == 0:
                if is_valid(puzzle, row, col, num):
                    puzzle[row][col] = num
                    if all(all(cell != 0 for cell in row) for row in puzzle):
                        print("축하합니다! 스도쿠를 완성했습니다.")
                        print_board(puzzle)
                        break
                else:
                    print("잘못된 숫자입니다. 다시 시도하세요.")
            else:
                print("해당 칸은 이미 채워져 있습니다.")
        except (ValueError, IndexError):
            print("입력이 잘못되었습니다. 다시 시도하세요.")