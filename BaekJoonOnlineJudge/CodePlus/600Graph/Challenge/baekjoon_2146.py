# https://www.acmicpc.net/problem/2146
# Solved Date: 20.04.28.

import sys
import collections

read = sys.stdin.readline
DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_bridge(board, dist_board, boundary):
    queue = collections.deque(boundary)
    dist_min = 200
    save_step = 0
    while queue:
        y, x, step = queue.popleft()
        # back tracking으로, step이 달라졌는데, dist_min이 바뀌었으면 종료한다.
        if dist_min != 200 and save_step != step:
            break
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]):
                value = board[new_y][new_x]
                if value == 0:
                    board[new_y][new_x] = board[y][x]
                    dist_board[new_y][new_x] = step + 1
                    queue.append((new_y, new_x, step + 1))
                elif value != board[y][x]:
                    dist_min = min(dist_min, dist_board[new_y][new_x] + dist_board[y][x])
        save_step = step
    return dist_min


def mark_island(board, dist_board, island_index, y, x):
    # board는 섬 index로 변경한다.
    # 섬 내의 거리 값은 0으로 설정한다.
    boundary = []
    queue = collections.deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]):
                if board[new_y][new_x] == 1:
                    board[new_y][new_x] = island_index
                    dist_board[new_y][new_x] = 0
                    queue.append((new_y, new_x))
                elif board[new_y][new_x] == 0:
                    boundary.append((y, x, 0))
    return boundary


def find_island(board, dist_board):
    # boundary를 두어, 큐의 초기값을 구해둔다.
    boundary = []
    island_index = 2
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                board[y][x] = island_index
                dist_board[y][x] = 0
                boundary.extend(mark_island(board, dist_board, island_index, y, x))
                island_index += 1
    return boundary


def main():
    arr_num = int(read().strip())
    board = []
    for _ in range(arr_num):
        board.append([int(x) for x in read().split()])
    dist_board = [[None for _ in board[0]] for _ in board]
    boundary = find_island(board, dist_board)
    print(find_bridge(board, dist_board, boundary))


if __name__ == '__main__':
    main()
