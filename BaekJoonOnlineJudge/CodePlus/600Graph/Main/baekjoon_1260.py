# https://www.acmicpc.net/problem/1260
# Solved Date: 20.04.21.

import sys
import collections
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def stack_dfs(ad_list, node):
    check = [False for _ in range(len(ad_list))]
    check[node] = True
    print(node, end=' ')
    stack = [(node, 0)]
    while stack:
        node, start = stack.pop()
        for index in range(start, len(ad_list[node])):
            next_node = ad_list[node][index]
            if not check[next_node]:
                check[next_node] = True
                print(next_node, end=' ')
                stack.append((node, index+1))
                stack.append((next_node, 0))
                break


def dfs(ad_list, check, node):
    check[node] = True
    print(node, end=' ')
    for next_index in ad_list[node]:
        if not check[next_index]:
            dfs(ad_list, check, next_index)


def bfs(ad_list, node):
    check = [False for _ in range(len(ad_list))]
    queue = collections.deque()
    check[node] = True
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for input_node in ad_list[node]:
            if not check[input_node]:
                check[input_node] = True
                queue.append(input_node)


def main(mode=''):
    v_num, e_num, start_node = (int(x) for x in read().split())
    ad_list = [[] for _ in range(v_num + 1)]

    for _ in range(e_num):
        node, con_node = (int(x) for x in read().split())
        ad_list[node].append(con_node)
        ad_list[con_node].append(node)

    for index in range(v_num):
        ad_list[index].sort()

    if mode == 'recursion':
        check = [False for _ in range(v_num + 1)]
        dfs(ad_list, check, start_node)
    else:
        stack_dfs(ad_list, start_node)
    print()
    bfs(ad_list, start_node)


if __name__ == '__main__':
    main('recursion')
