# https://www.acmicpc.net/problem/10026
# Solved Date: 20.06.08.

import sys
import collections

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def vision(graphic, visit, y, x, weakness=False):
    queue = collections.deque()
    visit[y][x] = True
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        color = graphic[y][x]
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(graphic) or nx < 0 or nx >= len(graphic[0]) or visit[ny][nx]:
                continue
            if weakness:
                if color == 'B':
                    if graphic[ny][nx] != color:
                        continue
                else:
                    if graphic[ny][nx] == 'B':
                        continue
            else:
                if graphic[ny][nx] != color:
                    continue
            visit[ny][nx] = True
            queue.append((ny, nx))


def find_grid(graphic):
    visit = [[False for _ in range(len(graphic[0]))] for _ in range(len(graphic))]
    weak_visit = [[False for _ in range(len(graphic[0]))] for _ in range(len(graphic))]
    count = 0
    weak_count = 0
    for y in range(len(graphic)):
        for x in range(len(graphic[0])):
            if not visit[y][x]:
                count += 1
                vision(graphic, visit, y, x)
            if not weak_visit[y][x]:
                weak_count += 1
                vision(graphic, weak_visit, y, x, True)
    return count, weak_count


def main():
    graphic_num = int(read().strip())
    graphic = [read().strip() for _ in range(graphic_num)]
    print(*find_grid(graphic))


if __name__ == '__main__':
    main()
