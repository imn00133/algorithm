# https://www.acmicpc.net/problem/1600
# Solved Date: 20.05.02.

import sys
import collections

read = sys.stdin.readline
HORSE_DYX = ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2))
MONKEY_DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def mark_board(dyx, queue, distance, board, knight_num, y, x, step):
    for dy, dx in dyx:
        new_y, new_x = y + dy, x + dx
        if 0 > new_y or new_y >= len(board) or 0 > new_x or new_x >= len(board[0]):
            continue
        if not distance[knight_num][new_y][new_x] and not board[new_y][new_x]:
            distance[knight_num][new_y][new_x] = step
            queue.append((knight_num, new_y, new_x))
            if new_y == len(board) - 1 and new_x == len(board[0]) - 1:
                return True
    return False


def explorer(knight_num, distance, board):
    if board[-1][-1] == 1:
        # 장애물로 갈 수 없을 때
        return -1
    elif len(board) == 1 and len(board[0]) == 1:
        # 최소값일 때
        return 0
    queue = collections.deque()
    distance[knight_num][0][0] = 1
    #  knight_num, y, x
    queue.append((knight_num, 0, 0))
    while queue:
        knight_num, y, x = queue.popleft()
        step = distance[knight_num][y][x]
        if mark_board(MONKEY_DYX, queue, distance, board, knight_num, y, x, step + 1):
            return step
        if knight_num > 0:
            knight_num -= 1
            if mark_board(HORSE_DYX, queue, distance, board, knight_num, y, x, step + 1):
                return step
    return -1


def main():
    knight_num = int(read().strip())
    column, row = (int(x) for x in read().split())
    board = []
    for _ in range(row):
        board.append([int(x) for x in read().split()])
    distance = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(knight_num + 1)]
    print(explorer(knight_num, distance, board))


if __name__ == '__main__':
    main()
