# https://www.acmicpc.net/problem/2580
# Solved Date: 20.05.22.

import sys
read = sys.stdin.readline

SQUARE_NUM = 9


def calc_square_num(y, x):
    return 3 * (y // 3) + (x // 3)


def init_main(board, row_possible, col_possible, square_possible):
    find_num_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            number = board[y][x]
            if number == 0:
                find_num_pos.append((y, x))
            else:
                row_possible[y][number] = False
                col_possible[x][number] = False
                square_possible[calc_square_num(y, x)][number] = False
    return find_num_pos


def recursion(board, find_num_pos, row_possible, col_possible, square_possible, index=0, exit_flag=False):
    if index == len(find_num_pos):
        return True
    y, x = find_num_pos[index]
    square_num = calc_square_num(y, x)
    for number in range(1, SQUARE_NUM + 1):
        if row_possible[y][number] and col_possible[x][number] and square_possible[square_num][number]:
            board[y][x] = number
            row_possible[y][number] = False
            col_possible[x][number] = False
            square_possible[square_num][number] = False
            exit_flag = recursion(board, find_num_pos, row_possible, col_possible, square_possible, index+1, exit_flag)
            row_possible[y][number] = True
            col_possible[x][number] = True
            square_possible[square_num][number] = True
            if exit_flag:
                break
    return exit_flag


def main():
    # 각 행은 그 row와 colum, squrare의 값이고, 숫자를 사용할 수 있는지 저장한다.
    row_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    col_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    # 왼쪽 위부터 012/345/678로 square의 숫자를 계산한다.
    square_possible = [[True for _ in range(SQUARE_NUM + 1)] for _ in range(SQUARE_NUM)]
    board = [[int(x) for x in read().split()] for _ in range(SQUARE_NUM)]
    find_num_pos = init_main(board, row_possible, col_possible, square_possible)
    recursion(board, find_num_pos, row_possible, col_possible, square_possible)
    for y in range(len(board)):
        print(*board[y], sep=' ')


if __name__ == '__main__':
    main()
