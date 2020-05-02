# https://www.acmicpc.net/problem/1167
# Solved Date: 20.05.01.

import sys
import collections

read = sys.stdin.readline


def bfs(tree, start=1):
    end_node = start
    max_len = 0
    check = [False for _ in range(len(tree))]
    queue = collections.deque()
    queue.append((start, max_len))
    check[start] = True
    while queue:
        node, end_len = queue.popleft()
        for index in range(0, len(tree[node]), 2):
            next_node = tree[node][index]
            node_len = tree[node][index + 1]
            if not check[next_node]:
                check[next_node] = True
                current_len = node_len + end_len
                if current_len > max_len:
                    max_len = current_len
                    end_node = next_node
                queue.append((next_node, current_len))
    return end_node, max_len


def main(mode=''):
    vertex_num = int(read().strip())
    tree = [[] for _ in range(vertex_num + 1)]
    for _ in range(vertex_num):
        temp = [int(x) for x in read().split()]
        tree[temp[0]].extend(temp[1:-1])
    if mode == 'bfs':
        end_node, max_len = bfs(tree)
        end_node, max_len = bfs(tree, end_node)
    else:
        max_len = post_order(tree)
    print(max_len)


if __name__ == '__main__':
    main()
