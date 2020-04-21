# https://www.acmicpc.net/problem/11724
# Solved Date: 20.04.21.

import sys
import collections
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def dfs(ad_list, check, node):
    for next_node in ad_list[node]:
        if not check[next_node]:
            check[next_node] = True
            dfs(ad_list, check, next_node)


def bfs(ad_list, check, node):
    queue = collections.deque()
    queue.append(node)
    check[node] = True
    while queue:
        node = queue.popleft()
        for next_node in ad_list[node]:
            if not check[next_node]:
                check[next_node] = True
                queue.append(next_node)


def main(mode=''):
    vertex, edge = (int(x) for x in read().split())
    ad_list = [[] for _ in range(vertex + 1)]
    for _ in range(edge):
        node, con_node = (int(x) for x in read().split())
        ad_list[node].append(con_node)
        ad_list[con_node].append(node)

    check = [False for _ in range(len(ad_list))]
    connect_count = 0
    if mode == 'dfs':
        for node in range(1, len(ad_list)):
            if not check[node]:
                connect_count += 1
                dfs(ad_list, check, node)
    else:
        for node in range(1, len(ad_list)):
            if not check[node]:
                connect_count += 1
                bfs(ad_list, check, node)
    print(connect_count)


if __name__ == '__main__':
    main('dfs')
