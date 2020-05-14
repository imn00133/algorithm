# https://www.acmicpc.net/problem/2805
# Solved Date: 20.05.14.

import sys
import collections
read = sys.stdin.readline


def cutting_tree(cut_length, trees):
    length = 0
    for tree in trees:
        if tree > cut_length:
            length += tree - cut_length
    return length


def fast_cutting_tree(cut_length, trees):
    # https://www.acmicpc.net/source/18949565 참고
    length = 0
    for tree in trees.keys():
        if tree > cut_length:
            length += (tree - cut_length) * trees[tree]
    return length


def binary_search(length, trees, mode):
    if mode == 'fast':
        cut_tree = fast_cutting_tree
    else:
        cut_tree = cutting_tree
    left = 0
    right = max(trees)
    while left < right:
        mid = (left + right) // 2 + 1
        if cut_tree(mid, trees) >= length:
            left = mid
        else:
            right = mid - 1
    return left


def main(mode=''):
    num, length = (int(x) for x in read().split())
    if mode == 'fast':
        trees = collections.Counter([int(x) for x in read().split()])
    else:
        trees = [int(x) for x in read().split()]
    print(binary_search(length, trees, mode))


if __name__ == '__main__':
    main('fast')
