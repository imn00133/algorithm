# https://www.acmicpc.net/problem/2178
# Solved Date: 20.04.22.

import sys
import collections

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(maze):
    queue = collections.deque()
    queue.append((0, 0))
    while queue:
        y, x = queue.popleft()
        step_count = maze[y][x]
        for dy, dx in DXY:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) and maze[new_y][new_x] == 1:
                maze[new_y][new_x] = step_count + 1
                queue.append((new_y, new_x))
        if maze[-1][-1] > 1:
            return maze[-1][-1]


def main():
    width, height = (int(x) for x in read().split())
    maze = []
    for _ in range(width):
        maze.append([int(x) for x in list(read().strip())])
    print(bfs(maze))


if __name__ == '__main__':
    main()
