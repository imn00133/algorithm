# https://www.acmicpc.net/problem/1697
# Solved Date: 20.04.29.
# https://www.acmicpc.net/source/17359841 참고
# https://www.acmicpc.net/source/16273492 참고

import sys
import collections
read = sys.stdin.readline
MAX = 100000


def bfs(start, end):
    if start >= end:
        return start - end
    dist = [-1 for _ in range(MAX + 1)]
    queue = collections.deque()
    queue.append(start)
    dist[start] = 0
    while queue:
        node = queue.popleft()
        step = dist[node] + 1
        for next_node in [node - 1, node + 1, node * 2]:
            if 0 <= next_node < len(dist):
                if dist[next_node] > 0:
                    continue
                elif next_node == end:
                    return step
                dist[next_node] = step
                queue.append(next_node)


def main():
    current_pos, find_pos = (int(x) for x in read().split())
    print(bfs(current_pos, find_pos))


if __name__ == '__main__':
    main()
