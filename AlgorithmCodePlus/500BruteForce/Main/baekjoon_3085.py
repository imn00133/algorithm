# https://www.acmicpc.net/problem/3085
# Solved Date: 20.04.04.

import sys
read = sys.stdin.readline


def line_count_candy(line):
    count_list = []
    count = 1
    for index in range(1, len(line)):
        if line[index] == line[index - 1]:
            count += 1
        else:
            count_list.append(count)
            count = 1
    count_list.append(count)
    return max(count_list)


def make_column_line(board, x):
    line = []
    for y in range(len(board)):
        line.append(board[y][x])
    return line


def all_line_count_candy(board, mode):
    candy_max_count_list = []
    if mode == 'row':
        for line in board:
            candy_max_count_list.append(line_count_candy(line))
    elif mode == 'column':
        for x in range(len(board)):
            candy_max_count_list.append(line_count_candy(make_column_line(board, x)))
    return candy_max_count_list


def change_row(board, y, x, count_all_list):
    # 행 방향 바꾸기
    board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
    # 변경된 count 합산
    count_all_list.append(line_count_candy(board[y]))
    count_all_list.append(line_count_candy(make_column_line(board, x)))
    count_all_list.append(line_count_candy(make_column_line(board, x+1)))
    board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
    return count_all_list


def change_column(board, y, x, count_all_list):
    # 열 방향 바꾸기
    board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
    # 변경된 count 합산
    count_all_list.append(line_count_candy(board[y]))
    count_all_list.append(line_count_candy(board[y+1]))
    count_all_list.append(line_count_candy(make_column_line(board, x)))
    board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
    return count_all_list


def brute_force(board):
    count_all_list = all_line_count_candy(board, 'row')
    count_all_list.extend(all_line_count_candy(board, 'column'))
    for y in range(len(board)-1):
        for x in range(len(board)-1):
            count_all_list = change_row(board, y, x, count_all_list)
            count_all_list = change_column(board, y, x, count_all_list)
    # 마지막을 주의한다.
    count_all_list = change_row(board, len(board)-1, len(board)-2, count_all_list)
    count_all_list = change_column(board, len(board)-2, len(board)-1, count_all_list)
    return max(count_all_list)


def main():
    board_size = int(read().strip())
    board = []
    for _ in range(board_size):
        board.append(list(read().strip()))
    print(brute_force(board))


if __name__ == '__main__':
    main()
