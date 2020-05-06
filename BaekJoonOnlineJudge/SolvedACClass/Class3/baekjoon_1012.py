# https://www.acmicpc.net/problem/1012
# Solved Date: 20.05.06.

import sys
import collections

read = sys.stdin.readline
DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def explorer(field, y, x):
    queue = collections.deque()
    field[y][x] = 0
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(field) and 0 <= new_x < len(field[0]) and field[new_y][new_x] == 1:
                field[new_y][new_x] = 0
                queue.append((new_y, new_x))


def planting_cabbage():
    column, row, cabbage_num = (int(x) for x in read().split())
    field = [[0 for _ in range(column)] for _ in range(row)]
    for _ in range(cabbage_num):
        x, y = (int(x) for x in read().split())
        field[y][x] = 1
    return field


def main():
    test_case = int(read().strip())
    for _ in range(test_case):
        field = planting_cabbage()
        count = 0
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == 1:
                    count += 1
                    explorer(field, y, x)
        print(count)


if __name__ == '__main__':
    main()
