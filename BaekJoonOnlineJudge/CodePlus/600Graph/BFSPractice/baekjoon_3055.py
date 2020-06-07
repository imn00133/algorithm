# https://www.acmicpc.net/problem/3055
# Solved Date: 20.06.07.

import sys
import collections

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def init(visit, start, water_pos, stone_pos):
    # 갈 수 없는 구역 설정
    for y, x in stone_pos:
        visit[y][x] = True
    # 물과 고슴도치를 넣음
    queue = collections.deque()
    clock = 0
    for y, x in water_pos:
        visit[y][x] = True
        # y, x, clock, 고슴도치인가?
        queue.append((y, x, clock, False))
    y, x = start
    visit[y][x] = True
    queue.append((y, x, clock, True))
    return queue


def simulation(board, start, end, water_pos, stone_pos):
    visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    queue = init(visit, start, water_pos, stone_pos)
    while queue:
        y, x, clock, hedgehog = queue.popleft()
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]) or visit[ny][nx]:
                continue
            if (ny, nx) == end:
                if hedgehog:
                    return clock + 1
                else:
                    continue
            visit[ny][nx] = True
            queue.append((ny, nx, clock + 1, hedgehog))
    return "KAKTUS"


def find_pos(board):
    start, end = (), ()
    stone_pos = []
    water_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            letter = board[y][x]
            if letter == '.':
                continue
            elif letter == 'S':
                start = (y, x)
            elif letter == 'D':
                end = (y, x)
            elif letter == 'X':
                stone_pos.append((y, x))
            else:
                water_pos.append((y, x))
    return start, end, water_pos, stone_pos


def main():
    row, col = (int(x) for x in read().split())
    board = [read().strip() for _ in range(row)]
    print(simulation(board, *find_pos(board)))


if __name__ == '__main__':
    main()
