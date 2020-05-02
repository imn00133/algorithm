# https://www.acmicpc.net/problem/13913
# Solved Date: 20.04.29.

import sys
import collections
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline
MAX = 100000


def back_tracing(start, node, move_pos):
    if start == node:
        return print(node, end=' ')
    prev_node = move_pos[node]
    back_tracing(start, prev_node, move_pos)
    return print(node, end=' ')


def bfs(start, end):
    dist = [-1 for _ in range(MAX + 1)]
    move_pos = [-1 for _ in range(MAX + 1)]
    queue = collections.deque()
    queue.append(start)
    dist[start] = 0
    move_pos[start] = start
    while queue:
        node = queue.popleft()
        step = dist[node] + 1
        for next_node in [node-1, node+1, node*2]:
            if 0 <= next_node < len(dist):
                if dist[next_node] >= 0:
                    continue
                elif next_node == end:
                    print(step)
                    move_pos[next_node] = node
                    return move_pos
                else:
                    dist[next_node] = step
                    move_pos[next_node] = node
                    queue.append(next_node)


def main():
    start, end = (int(x) for x in read().split())
    if start < end:
        move_pos = bfs(start, end)
        back_tracing(start, end, move_pos)
    else:
        print(start - end)
        for num in range(start, end-1, -1):
            print(num, end=' ')


if __name__ == '__main__':
    main()
