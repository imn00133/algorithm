# https://www.acmicpc.net/problem/2250
# Sovled Date: 20.05.01.

import sys
from collections import defaultdict

read = sys.stdin.readline
MAX = 10000


def find_ans(tree_meta):
    min_level = MAX + 1
    max_width = 0
    for level in tree_meta.keys():
        width = tree_meta[level][-1] - tree_meta[level][0] + 1
        if max_width <= width:
            min_level = min(min_level, level)
            max_width = width
    return min_level, max_width


def explorer(adj_list, root):
    # dfs
    tree_mata = defaultdict(list)
    # node, 왼쪽 순회 확인, 레벨
    stack = [(root, False, 1)]
    column = 1
    while stack:
        node, right_flag, level = stack.pop()
        if node == -1:
            continue
        elif right_flag:
            tree_mata[level].append(column)
            column += 1
            stack.append((adj_list[node][1], False, level + 1))
        else:
            stack.append((node, True, level))
            stack.append((adj_list[node][0], False, level + 1))
    return tree_mata


def check_root(adj_list):
    root = [True for _ in range(len(adj_list) - 1)]
    for index in range(1, len(adj_list)):
        for j in range(2):
            node = adj_list[index][j]
            if node != -1:
                root[node-1] = False
    for index, flag in enumerate(root, 1):
        if flag:
            return index


def input_value():
    arr_num = int(read().strip())
    adj_list = [[] for _ in range(arr_num + 1)]
    for _ in range(arr_num):
        temp = [int(x) for x in read().split()]
        adj_list[temp[0]] = temp[1:]
    return adj_list


def main():
    adj_list = input_value()
    tree_meta = explorer(adj_list, check_root(adj_list))
    print(*find_ans(tree_meta), sep=' ')


if __name__ == '__main__':
    main()
