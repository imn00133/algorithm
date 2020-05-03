# https://www.acmicpc.net/problem/11725
# Solved Date: 20.05.01.

import sys
import collections

read = sys.stdin.readline


def find_parent(adj_list):
    check = [False for _ in range(len(adj_list))]
    parents = [0 for _ in range(len(adj_list))]
    queue = collections.deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for next_node in adj_list[node]:
            if check[next_node]:
                continue
            check[next_node] = True
            parents[next_node] = node
            queue.append(next_node)
    return parents


def main():
    node_num = int(read().strip())
    adj_list = [[] for _ in range(node_num + 1)]
    for _ in range(node_num - 1):
        node, con_node = (int(x) for x in read().split())
        adj_list[node].append(con_node)
        adj_list[con_node].append(node)
    parents = find_parent(adj_list)
    for node in range(2, node_num + 1):
        print(parents[node])


if __name__ == '__main__':
    main()
