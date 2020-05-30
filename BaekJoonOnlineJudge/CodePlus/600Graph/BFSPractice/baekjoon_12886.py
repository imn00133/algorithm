# https://www.acmicpc.net/problem/12886
# Solved Date: 20.05.30.

import sys
import collections

read = sys.stdin.readline
MAX = 500


def stones_sorting(queue, visit, stones):
    stones = sorted(stones)
    if not visit[stones[0]][stones[1]][stones[2]]:
        visit[stones[0]][stones[1]][stones[2]] = True
        queue.append(stones)


def game_loop(stones):
    visit = [[[False for _ in range(MAX + 1)] for _ in range(MAX + 1)] for _ in range(MAX + 1)]
    queue = collections.deque()
    stones.sort()
    visit[stones[0]][stones[1]][stones[2]] = True
    queue.append(stones)
    while queue:
        x, y, z = queue.popleft()
        if x == y and y == z:
            return 1
        if y - x > 0:
            dx = x + x
            dy = y - x
            stones = [dx, dy, z]
            stones_sorting(queue, visit, stones)
        if z - x > 0:
            dx = x + x
            dz = z - x
            stones = [dx, y, dz]
            stones_sorting(queue, visit, stones)
        if y - z > 0:
            dy = y + y
            dz = z - y
            stones = [x, dy, dz]
            stones_sorting(queue, visit, stones)
    return 0


def main():
    stones = [int(x) for x in read().split()]
    print(game_loop(stones))


if __name__ == '__main__':
    main()
