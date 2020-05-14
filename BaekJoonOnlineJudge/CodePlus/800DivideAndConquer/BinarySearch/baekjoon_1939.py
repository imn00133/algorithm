# https://www.acmicpc.net/problem/1939
# Solved Date: 20.05.14.

import sys
import collections

read = sys.stdin.readline


def pass_islands(islands, weight, start, end):
    check = [False for _ in range(len(islands))]
    queue = collections.deque()
    check[start] = True
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for next_node, bridge_weight in islands[node]:
            if not check[next_node] and bridge_weight >= weight:
                check[next_node] = True
                queue.append(next_node)
    return False


def binary_search(islands, max_weight, start, end):
    left = 1
    right = max_weight
    while left < right:
        mid = (left + right) // 2 + 1
        if pass_islands(islands, mid, start, end):
            left = mid
        else:
            right = mid - 1
    return left


def explore(islands, start, end):
    # 시간초과 python3/pypy3
    check = [0 for _ in range(len(islands))]
    queue = collections.deque()
    for next_node, bridge_weight in islands[start]:
        if bridge_weight > check[next_node]:
            check[next_node] = bridge_weight
            queue.append((next_node, bridge_weight))
            if bridge_weight > check[start]:
                check[start] = bridge_weight
    while queue:
        node, weight = queue.popleft()
        for next_node, bridge_weight in islands[node]:
            if bridge_weight >= weight:
                move_weight = weight
            else:
                move_weight = bridge_weight
            if move_weight > check[next_node]:
                check[next_node] = move_weight
                queue.append((next_node, move_weight))
    return check[end]


def main(mode=''):
    island_num, bridge_num = (int(x) for x in read().split())
    islands = [[] for _ in range(island_num + 1)]
    max_weight = 0
    for _ in range(bridge_num):
        node, con_node, weight = (int(x) for x in read().split())
        islands[node].append((con_node, weight))
        islands[con_node].append((node, weight))
        if max_weight < weight:
            max_weight = weight
    start, end = (int(x) for x in read().split())
    if mode == 'binary':
        print(binary_search(islands, max_weight, start, end))
    else:
        print(explore(islands, start, end))


if __name__ == '__main__':
    main('binary')
