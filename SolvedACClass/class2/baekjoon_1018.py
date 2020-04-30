# https://www.acmicpc.net/problem/1018
# Solved Date: 20.04.30.

import sys
read = sys.stdin.readline


def check_board(board, y, x):
    white_start = 0
    black_start = 0
    # y가 짝수이면 black과 같을 때 white가 증가한다.
    # y가 홀수이면 black과 같을 때 black이 증가한다.
    black = "BWBWBWBW"
    for dy in range(8):
        if dy % 2 == 0:
            for dx in range(8):
                new_y, new_x = y + dy, x + dx
                if board[new_y][new_x] == black[dx]:
                    white_start += 1
                else:
                    black_start += 1
        else:
            for dx in range(8):
                new_y, new_x = y + dy, x + dx
                if board[new_y][new_x] == black[dx]:
                    black_start += 1
                else:
                    white_start += 1
    return min(black_start, white_start)


def brute_force(board):
    # 완전히 하나의 색에서 하나라도 다른 색이 칠해지면 가지수 1이 감소한다.
    min_count = 32
    for y in range(len(board) - 7):
        for x in range(len(board[0]) - 7):
            min_count = min(min_count, check_board(board, y, x))
    return min_count


def main(mode=''):
    row, column = (int(x) for x in read().split())
    board = []
    for _ in range(row):
        board.append(read().strip())
    if mode == 'brute':
        ans = brute_force(board)
    else:
        ans = bottom_up(board)
    print(ans)


if __name__ == '__main__':
    main('brute')
