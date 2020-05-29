# https://www.acmicpc.net/problem/16948
# Solved Date: 20.05.29.

import sys
import collections

read = sys.stdin.readline
DYX = ((-2, -1), (-2, 1), (0, 2), (2, 1), (2, -1), (0, -2))


def explorer(board, start, end):
    queue = collections.deque()
    queue.append(start)
    board[start[0]][start[1]] = 0
    while queue:
        y, x = queue.popleft()
        count = board[y][x] + 1
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board) or board[ny][nx] > -1:
                continue
            next_node = (ny, nx)
            if next_node == end:
                return count
            board[ny][nx] = count
            queue.append(next_node)
    return -1


def main():
    board_num = int(read().strip())
    board = [[-1 for _ in range(board_num)] for _ in range(board_num)]
    temp_pos = [int(x) for x in read().split()]
    start, end = (temp_pos[0], temp_pos[1]), (temp_pos[2], temp_pos[3])
    print(explorer(board, start, end))


if __name__ == '__main__':
    main()
