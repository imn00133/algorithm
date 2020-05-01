# https://www.acmicpc.net/problem/2250
# Sovled Date: 20.05.01.

import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline
MAX = 10000


def find_ans(tree_meta):
    min_level = MAX + 1
    max_width = 0
    meta_key = tree_meta.keys()
    for level in sorted(meta_key):
        # 맨 마지막이 최대, 맨 첫번째가 최소임이 보장된다.
        width = tree_meta[level][-1] - tree_meta[level][0] + 1
        if max_width < width:
            min_level = level
            max_width = width
    return min_level, max_width


def explorer(adj_list, root):
    # defaultdict은 키가 없을 경우 빈 리스트를 작성하여 값을 초기화해준다.
    tree_meta = defaultdict(list)
    # node, 왼쪽 순회 점검, 레벨
    stack = [(root, False, 1)]
    column = 1
    while stack:
        node, right_flag, level = stack.pop()
        if node == -1:
            continue
        elif right_flag:
            # in order 순회를 함으로, column값을 저장한 뒤, 값을 1증가시킨다.
            tree_meta[level].append(column)
            column += 1
            stack.append((adj_list[node][1], False, level + 1))
        else:
            stack.append((node, True, level))
            stack.append((adj_list[node][0], False, level + 1))
    return tree_meta


def recursion_explorer(adj_list, tree_meta, node, column=1, level=1):
    if node == -1:
        return column
    column = recursion_explorer(adj_list, tree_meta, adj_list[node][0], column, level+1)
    tree_meta[level].append(column)
    column += 1
    column = recursion_explorer(adj_list, tree_meta, adj_list[node][1], column, level+1)
    return column


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
    adj_list = [None for _ in range(arr_num + 1)]
    for _ in range(arr_num):
        node, *binary = (int(x) for x in read().split())
        adj_list[node] = binary
    return adj_list


def main(mode=''):
    adj_list = input_value()
    if mode == 'recursive':
        tree_meta = defaultdict(list)
        recursion_explorer(adj_list, tree_meta, check_root(adj_list))
    else:
        tree_meta = explorer(adj_list, check_root(adj_list))
    print(*find_ans(tree_meta), sep=' ')


if __name__ == '__main__':
    main('recursive')
