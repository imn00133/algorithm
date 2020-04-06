# https://www.acmicpc.net/problem/14500
# Solved Date

import sys

# y, x순/ 상대위치이다.
# 그림 순서대로 표현하였다. 막대기 2개, 네모 1개, L자 8개, 번개모양 4개, 요철모양 4개
# 0, 0을 기준으로 표현하였다.
BLOCKS = (((0, 0), (0, 1), (0, 2), (0, 3)),
          ((0, 0), (1, 0), (2, 0), (3, 0)),
          # 네모
          ((0, 0), (0, 1), (1, 0), (1, 1)),
          # L자
          ((0, 0), (1, 0), (2, 0), (2, 1)),
          ((0, 0), (0, 1), (0, 2), (1, 0)),
          ((0, 2), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (0, 1), (1, 1), (2, 1)),
          # L자 대칭
          ((0, 1), (1, 1), (2, 0), (2, 1)),
          ((0, 0), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (0, 1), (1, 0), (2, 0)),
          ((0, 0), (0, 1), (0, 2), (1, 2)),
          # 번개
          ((0, 0), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (0, 2), (1, 0), (1, 1)),
          # 번개 대칭
          ((0, 1), (1, 0), (1, 1), (2, 0)),
          ((0, 0), (0, 1), (1, 1), (1, 2)),
          # 요철모양
          ((0, 0), (0, 1), (0, 2), (1, 1)),
          ((0, 1), (1, 0), (1, 1), (2, 1)),
          ((0, 1), (1, 0), (1, 1), (1, 2)),
          ((0, 0), (1, 0), (1, 1), (2, 0)),)


def draw():
    # 제대로 그렸는지 확인
    for index, shape in enumerate(BLOCKS):
        arr = [[0 for _ in range(4)] for _ in range(4)]
        print("index:", index)
        for pos in shape:
            arr[pos[0]][pos[1]] = 1
        for line in arr:
            for value in line:
                if value == 0:
                    value = ' '
                print(value, end='')
            print()
        print()


def calc_tetromino_sum(board, BLOCK):
    max_score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            score = 0
            for pos in BLOCK:
                rel_y = y + pos[0]
                rel_x = x + pos[1]
                if rel_y >= len(board):
                    break
                elif rel_x >= len(board[0]):
                    continue
                else:
                    score += board[rel_y][rel_x]
            max_score = max(max_score, score)
    return max_score


def brute_force(board):
    max_score = 0
    for BLOCK in BLOCKS:
        max_score = max(max_score, calc_tetromino_sum(board, BLOCK))
    return max_score


def main(mode=''):
    read = sys.stdin.readline
    file = None
    if mode == 'f':
        file = open("baekjoon_14500_input.txt", mode='r', encoding='utf-8')
        read = file.readline
    n, m = (int(x) for x in read().split())
    board = []
    for _ in range(n):
        board.append([int(x) for x in read().split()])
    print(brute_force(board))
    if mode == 'f':
        file.close()


if __name__ == '__main__':
    main()
