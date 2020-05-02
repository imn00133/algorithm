# https://www.acmicpc.net/problem/1707
# Solved Date: 20.04.21.

import sys
import collections
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline


def dfs(ad_list):
    check = [0 for _ in range(len(ad_list))]
    stack = []
    for node in range(len(ad_list)):
        if not check[node]:
            check[node] = 1
            stack.append((node, 0))
        while stack:
            node, index = stack.pop()
            for next_index in range(index, len(ad_list[node])):
                next_node = ad_list[node][next_index]
                if not check[next_node]:
                    check[next_node] = 3 - check[node]
                    stack.append((node, next_index))
                    stack.append((next_node, 0))
                    break
                elif check[next_node] == check[node]:
                    return "NO"
    return "YES"


def bfs(ad_list):
    check = [0 for _ in range(len(ad_list))]
    queue = collections.deque()
    for node in range(len(ad_list)):
        if not check[node]:
            check[node] = 1
            queue.append(node)
        while queue:
            node = queue.popleft()
            for next_node in ad_list[node]:
                if not check[next_node]:
                    check[next_node] = 3 - check[node]
                    queue.append(next_node)
                elif check[next_node] == check[node]:
                    return "NO"
    return "YES"


def main(mode=''):
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        vertex, edge = (int(x) for x in read().split())
        ad_list = [[] for _ in range(vertex + 1)]
        for _ in range(edge):
            node, con_node = (int(x) for x in read().split())
            ad_list[node].append(con_node)
            ad_list[con_node].append(node)
        if mode == 'dfs':
            print(dfs(ad_list))
        else:
            print(bfs(ad_list))


if __name__ == '__main__':
    main('dfs')
