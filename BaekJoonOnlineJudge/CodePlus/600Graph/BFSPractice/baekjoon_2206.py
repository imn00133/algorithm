# https://www.acmicpc.net/problem/2206
# Solved Date: 20.05.30.

import sys
import collections

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))
MAX = 1000 ** 2


def explorer(board):
    visit = [[[MAX for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(2)]
    queue = collections.deque()
    visit[1][0][0] = 1
    # 부실 수 있는 벽 개수, y , x
    queue.append((1, 0, 0))
    while queue:
        wall_broken, y, x = queue.popleft()
        step = visit[wall_broken][y][x]
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]) or visit[wall_broken][ny][nx] != MAX:
                continue
            if board[ny][nx] == 0:
                visit[wall_broken][ny][nx] = step + 1
                queue.append((wall_broken, ny, nx))
            elif wall_broken > 0:
                visit[wall_broken-1][ny][nx] = step + 1
                queue.append((wall_broken - 1, ny, nx))
    ans = min(visit[0][-1][-1], visit[1][-1][-1])
    if ans == MAX:
        ans = -1
    return ans


def fast_explorer(board):
    visit = [[MAX for _ in range(len(board[0]))] for _ in range(len(board))]
    queue = collections.deque()
    visit[0][0] = 1
    # y, x, 벽을 부술 수 있는가?
    queue.append((0, 0, True))
    while queue:
        y, x, possible_broken = queue.popleft()
        step = visit[y][x]
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
                continue
            if visit[ny][nx] != MAX and step + 1 >= visit[ny][nx]:
                continue
            if board[ny][nx] == 0:
                visit[ny][nx] = step + 1
                queue.appendleft((ny, nx, possible_broken))
            elif possible_broken:
                visit[ny][nx] = step + 1
                queue.append((ny, nx, not possible_broken))
    ans = visit[-1][-1]
    if ans == MAX:
        ans = -1
    return ans


def main():
    row, col = (int(x) for x in read().split())
    board = [[int(x) for x in read().strip()] for _ in range(row)]
    print(fast_explorer(board))


if __name__ == '__main__':
    main()
