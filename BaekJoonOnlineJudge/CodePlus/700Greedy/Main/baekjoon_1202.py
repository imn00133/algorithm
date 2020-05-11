# https://www.acmicpc.net/problem/1202
# Solved Date: 20.05.11.

import sys
import operator
import heapq

read = sys.stdin.readline


class Jewel:
    def __init__(self, weight, value=0, bag=False):
        self.weight = weight
        self.value = value
        self.bag = bag

    def __str__(self):
        return f"{self.weight}, {self.value}, {self.bag}"

    def __repr__(self):
        return f"Jewel({self.weight}, {self.value}, {self.bag})"

    def __lt__(self, other):
        return self.weight < other.weight or (self.weight == other.weight and self.value < other.value)

    def __gt__(self, other):
        return self.weight > other.weight or (self.weight == other.weight and self.value < other.value)


def max_heap():
    gem_num, bag_num = (int(x) for x in read().split())
    gems = [Jewel(*(int(x) for x in read().split())) for _ in range(gem_num)]
    # gems.sort(key=operator.attrgetter('value'), reverse=True)
    gems.extend(Jewel(*(int(x) for x in read().split()), 0, True) for _ in range(bag_num))
    gems.sort()
    print(gems)


def main(mode=''):
    if mode == 'max_heap':
        max_heap()


if __name__ == '__main__':
    main('max_heap')
