# https://www.acmicpc.net/problem/17142
# Solved Date: 20.05.06.

import sys
import collections
import itertools

read = sys.stdin.readline
MAX = 2500
DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def explore(board, step_board, select_pos):
    count = 0
    queue = collections.deque()
    for y, x in select_pos:
        step_board[y][x] = count
        queue.append((y, x, count))
    while queue:
        y, x, current_count = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and step_board[new_y][new_x] == -1:
                if board[new_y][new_x] == 0:
                    next_count = current_count + 1
                    if count < next_count:
                        count = next_count
                    step_board[new_y][new_x] = next_count
                    queue.append((new_y, new_x, next_count))
                elif board[new_y][new_x] == 2:
                    next_count = current_count + 1
                    step_board[new_y][new_x] = next_count
                    queue.append((new_y, new_x, next_count))
    for y in range(len(step_board)):
        for x in range(len(step_board[0])):
            if step_board[y][x] == -1 and board[y][x] == 0:
                return MAX
    return count


def find_virus(board):
    # bfs
    virus_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 2:
                virus_pos.append((y, x))
    return virus_pos


def main():
    arr_num, active_virus = (int(x) for x in read().split())
    board = []
    for _ in range(arr_num):
        board.append([int(x) for x in read().split()])
    virus_pos = find_virus(board)
    step = MAX
    for select_pos in itertools.combinations(virus_pos, active_virus):
        step_board = [[-1 for _ in range(len(board))] for _ in range(len(board[0]))]
        step = min(step, explore(board, step_board, select_pos))
    if step == MAX:
        print(-1)
    else:
        print(step)


if __name__ == '__main__':
    main()
