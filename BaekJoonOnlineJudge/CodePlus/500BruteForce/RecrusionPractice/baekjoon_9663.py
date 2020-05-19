# https://www.acmicpc.net/problem/9663
# Solved Date: 20.05.19.

import sys
read = sys.stdin.readline


def batch_impossible_pos(impossible_pos, row, column, assign=True):
    for y in range(row, len(impossible_pos)):
        impossible_pos[y][column][0] = assign
    for index in range(1, len(impossible_pos)):
        y = row + index
        x = column + index
        if y >= len(impossible_pos) or x >= len(impossible_pos[0]):
            break
        impossible_pos[y][x][1] = assign
    for index in range(1, len(impossible_pos)):
        y = row + index
        x = column - index
        if y >= len(impossible_pos) or x < 0:
            break
        impossible_pos[y][x][2] = assign


def recursion(board_num, impossible_pos, row=0):
    if row == board_num:
        return 1
    count = 0
    for column in range(board_num):
        if any(impossible_pos[row][column]):
            continue
        batch_impossible_pos(impossible_pos, row, column)
        count += recursion(board_num, impossible_pos, row + 1)
        batch_impossible_pos(impossible_pos, row, column, assign=False)
    return count


def main():
    board_num = int(read().strip())
    # 열, 오른쪽 대각선, 왼쪽 대각선
    impossible_pos = [[[False for _ in range(3)] for _ in range(board_num)] for _ in range(board_num)]
    print(recursion(board_num, impossible_pos))


if __name__ == '__main__':
    main()
