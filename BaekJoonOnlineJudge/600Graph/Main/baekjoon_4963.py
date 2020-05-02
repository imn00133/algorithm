#
# Solved Date: 20.04.22.

import sys
import collections
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline
DXY = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))


def dfs(land, y, x):
    land[y][x] = 0
    count = 1
    for dy, dx in DXY:
        new_y = y + dy
        new_x = x + dx
        if 0 <= new_y < len(land) and 0 <= new_x < len(land[0]) and land[new_y][new_x]:
            count += dfs(land, new_y, new_x)
    return count


def bfs(land, y, x):
    queue = collections.deque()
    queue.append((y, x))
    land[y][x] = 0
    count = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in DXY:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(land) and 0 <= new_x < len(land[0]) and land[new_y][new_x]:
                land[new_y][new_x] = 0
                count += 1
                queue.append((new_y, new_x))
    return count


def main(mode=''):
    while True:
        width, height = (int(x) for x in read().split())
        land = []
        if not width and not height:
            break
        for _ in range(height):
            land.append([int(x) for x in read().split()])
        ans = []
        if mode == 'dfs':
            for y in range(len(land)):
                for x in range(len(land[0])):
                    if land[y][x] == 1:
                        ans.append(dfs(land, y, x))
        else:
            for y in range(len(land)):
                for x in range(len(land[0])):
                    if land[y][x] == 1:
                        ans.append(bfs(land, y, x))
        print(len(ans))


if __name__ == '__main__':
    main('dfs')
