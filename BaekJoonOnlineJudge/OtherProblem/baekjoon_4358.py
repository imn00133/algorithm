# https://www.acmicpc.net/problem/4358
# Solved Date: 20.04.25.

import sys
import collections

read = sys.stdin.readline


def main():
    trees = collections.defaultdict(int)
    trees_count = 0
    while True:
        tree_name = read().strip()
        if tree_name == '':
            break
        trees[tree_name] += 1
        trees_count += 1
    items = sorted(trees.items())
    for name, count in items:
        print("{0} {1:0.4f}".format(name, count / trees_count * 100))


if __name__ == '__main__':
    main()
