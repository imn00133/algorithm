# https://www.acmicpc.net/problem/16929
# Solved Date: 20.04.23.

import sys
import collections
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(board, check, y, x):
    queue = collections.deque()
    queue.append((y, x))
    check[y][x] = True
    ans = False
    while queue:
        y, x = queue.popleft()
        letter = board[y][x]
        board[y][x] = ''
        for dy, dx in DXY:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and board[new_y][new_x] == letter:
                if check[new_y][new_x]:
                    ans = True
                    queue.clear()
                    break
                else:
                    check[new_y][new_x] = True
                    queue.append((new_y, new_x))
    return ans


def entire_loop(board):
    check = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    ans = False
    for y in range(len(board)):
        for x in range(len(board[0])):
            if not check[y][x]:
                ans = bfs(board, check, y, x)
            if ans:
                return "Yes"
    return "No"


def main(mode=''):
    row, column = (int(x) for x in read().split())
    board = []
    for _ in range(row):
        board.append(list(read().strip()))
    print(entire_loop(board))


if __name__ == '__main__':
    main()
