# https://www.acmicpc.net/problem/7576
# Solved Date: 20.04.22.

import sys
import collections

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def explore_box(box, find_value):
    pos = []
    for y in range(len(box)):
        for x in range(len(box[0])):
            if box[y][x] == find_value:
                pos.append((y, x))
    return pos


def bfs(box):
    init_pos = explore_box(box, 1)
    queue = collections.deque(init_pos)
    day = 0
    while queue:
        y, x = queue.popleft()
        day = box[y][x]
        for dy, dx in DXY:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(box) and 0 <= new_x < len(box[0]) and not box[new_y][new_x]:
                box[new_y][new_x] = day + 1
                queue.append((new_y, new_x))
    if explore_box(box, 0):
        day = 0
    return day - 1


def main():
    width, height = (int(x) for x in read().split())
    box = []
    for _ in range(height):
        box.append([int(x) for x in read().split()])
    print(bfs(box))


if __name__ == '__main__':
    main()
