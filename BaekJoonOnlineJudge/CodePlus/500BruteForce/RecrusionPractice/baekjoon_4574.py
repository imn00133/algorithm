# https://www.acmicpc.net/problem/4574
# Solved Date: 20.05.22.

import sys
read = sys.stdin.readline

SQUARE_NUM = 9


def init():
    # 가능한지 확인을 위한 배열
    row_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    col_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    # 왼쪽 위부터 9칸을 012/345/678로 나눈다.
    square_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    # 사용한 도미노를 dictionary로 표시한다.
    # 숫자가 같은 경우는 미리 False로 제거한다.
    domino_possible = {}
    for num in range(SQUARE_NUM + 1):
        for co_num in range(SQUARE_NUM + 1):
            if num == co_num:
                domino_possible[(num, co_num)] = False
            else:
                domino_possible[(num, co_num)] = True
                domino_possible[(co_num, num)] = True
    board = [[0 for _ in range(SQUARE_NUM)] for _ in range(SQUARE_NUM)]
    return row_possible, col_possible, square_possible, domino_possible, board


def convert_pos(pos):
    y = ord(pos[0]) - ord('A')
    x = int(pos[1]) - 1
    return y, x


def read_domino(board, row_possible, col_possible, square_possible, domino_possible):
    domino = read().split()
    nums = []
    for index in range(0, len(domino), 2):
        number = int(domino[index])
        nums.append(number)
        y, x = convert_pos(domino[index+1])
        board[y][x] = number
        possible_convert(row_possible, col_possible, square_possible, (y, x), number)
    domino_possible[(nums[0], nums[1])] = False
    domino_possible[(nums[1], nums[0])] = False


def read_number(board, row_possible, col_possible, square_possible):
    position = read().split()
    for number, pos in enumerate(position, 1):
        y, x = convert_pos(pos)
        board[y][x] = number
        possible_convert(row_possible, col_possible, square_possible, (y, x), number)


def calc_square_num(y, x):
    return 3 * (y // 3) + (x // 3)


def possible_convert(row_possible, col_possible, square_possible, pos, number):
    y, x = pos
    row_possible[y][number] = not row_possible[y][number]
    col_possible[x][number] = not col_possible[x][number]
    square_num = calc_square_num(y, x)
    square_possible[square_num][number] = not square_possible[square_num][number]


def change_board(row_possible, col_possible, square_possible, domino_possible, num_pos, co_pos, num, co_num):
    possible_convert(row_possible, col_possible, square_possible, num_pos, num)
    possible_convert(row_possible, col_possible, square_possible, co_pos, co_num)
    domino_possible[(num, co_num)] = not domino_possible[(num, co_num)]
    domino_possible[(co_num, num)] = not domino_possible[(co_num, num)]


def check_possible(row_possible, col_possible, square_possible, y, x, number):
    square_num = calc_square_num(y, x)
    return row_possible[y][number] and col_possible[x][number] and square_possible[square_num][number]


def recursion(board, row_poss, col_poss, square_poss, domino_poss, index=0, exit_flag=False):
    if index == 81:
        return True
    y = index // 9
    x = index % 9
    if board[y][x] > 0:
        exit_flag = recursion(board, row_poss, col_poss, square_poss, domino_poss, index+1, exit_flag)
    else:
        for num in range(1, SQUARE_NUM + 1):
            if not check_possible(row_poss, col_poss, square_poss, y, x, num):
                continue
            for co_num in range(1, SQUARE_NUM + 1):
                if not domino_poss[(num, co_num)]:
                    continue
                for dy, dx in ((1, 0), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if ny >= len(board) or nx >= len(board[0]) or board[ny][nx]\
                            or not check_possible(row_poss, col_poss, square_poss, ny, nx, co_num):
                        continue
                    change_board(row_poss, col_poss, square_poss, domino_poss, (y, x), (ny, nx), num, co_num)
                    board[y][x] = num
                    board[ny][nx] = co_num
                    exit_flag = recursion(board, row_poss, col_poss, square_poss, domino_poss, index+1, exit_flag)
                    if exit_flag:
                        return exit_flag

                    change_board(row_poss, col_poss, square_poss, domino_poss, (y, x), (ny, nx), num, co_num)
                    board[y][x] = 0
                    board[ny][nx] = 0
    return exit_flag


def main():
    count = 0
    while True:
        domino_num = int(read().strip())
        if not domino_num:
            break
        count += 1
        row_possible, col_possible, square_possible, domino_possible, board = init()
        for _ in range(domino_num):
            read_domino(board, row_possible, col_possible, square_possible, domino_possible)
        read_number(board, row_possible, col_possible, square_possible)
        recursion(board, row_possible, col_possible, square_possible, domino_possible)
        print(f'Puzzle {count}')
        for line in board:
            print(*line, sep='')


if __name__ == '__main__':
    main()
