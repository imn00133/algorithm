# https://www.acmicpc.net/problem/1261
# Solved Date: 20.04.30.

import sys
import collections
read = sys.stdin.readline

DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(maze):
    deck = collections.deque()
    # y, x, broken_wall
    deck.appendleft((0, 0, 0))
    maze[0][0] = -1
    while deck:
        y, x, broken_wall = deck.popleft()
        # 좀 더 빨리 끝내고 싶었으나, 0, 0일 때를 따로 해결하지 않으려면, 속도를 희생한다.
        if y == len(maze) - 1 and x == len(maze[0]) - 1:
            return broken_wall
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) and maze[new_y][new_x] != -1:
                if maze[new_y][new_x] == 0:
                    maze[new_y][new_x] = -1
                    deck.appendleft((new_y, new_x, broken_wall))
                else:
                    maze[new_y][new_x] = -1
                    deck.append((new_y, new_x, broken_wall + 1))


def main():
    column, row = (int(x) for x in read().split())
    maze = []
    for _ in range(row):
        maze.append([int(x) for x in list(read().strip())])
    print(bfs(maze))


if __name__ == '__main__':
    main()
