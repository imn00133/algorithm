# https://www.acmicpc.net/problem/7562
# Solved Date: 20.04.22.

import sys
import collections

read = sys.stdin.readline
DXY = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))


def bfs(board, init_pos, end_pos):
    queue = collections.deque()
    queue.append(init_pos)
    end_y, end_x = end_pos
    while queue:
        y, x = queue.popleft()
        step = board[y][x]
        for dy, dx in DXY:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and not board[new_y][new_x]:
                board[new_y][new_x] = step + 1
                queue.append((new_y, new_x))
            if new_y == end_y and new_x == end_x:
                queue = collections.deque()
    return board[end_y][end_x]


def main():
    test_case = int(read().strip())
    for _ in range(test_case):
        board_num = int(read().strip())
        init_pos = [int(x) for x in read().split()]
        end_pos = [int(x) for x in read().split()]
        board = [[0 for _ in range(board_num)] for _ in range(board_num)]
        if init_pos == end_pos:
            step = 0
        else:
            step = bfs(board, init_pos, end_pos)
        print(step)


if __name__ == '__main__':
    main()
