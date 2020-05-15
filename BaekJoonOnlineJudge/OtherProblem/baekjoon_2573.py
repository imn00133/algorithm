# https://www.acmicpc.net/problem/2573
# Solved Date: 20.05.15.

import sys
import collections

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def melt_ice(iceberg, visit, y, x):
    queue = collections.deque()
    visit[y][x] = True
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(iceberg) and 0 <= new_x < len(iceberg[0]) and not visit[new_y][new_x]:
                if iceberg[new_y][new_x] == 0:
                    if iceberg[y][x] > 0:
                        iceberg[y][x] -= 1
                else:
                    visit[new_y][new_x] = True
                    queue.append((new_y, new_x))


def time(iceberg):
    current_time = 0
    count = 1
    while count == 1:
        current_time += 1
        count = 0
        visit = [[False for _ in range(len(iceberg[0]))] for _ in range(len(iceberg))]
        for y in range(len(iceberg)):
            for x in range(len(iceberg[0])):
                if iceberg[y][x] > 0 and not visit[y][x]:
                    count += 1
                    melt_ice(iceberg, visit, y, x)
    if count > 0:
        ans = current_time - 1
    else:
        ans = 0
    return ans


def main():
    row, column = (int(x) for x in read().split())
    iceberg = [[int(x) for x in read().split()] for _ in range(row)]
    print(time(iceberg))


def test():
    N, M = map(int, sys.stdin.readline().split())
    ice = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    print(ice)


if __name__ == '__main__':
    test()
    main()
