# https://www.acmicpc.net/problem/1202
# Solved Date: 20.05.11.

import sys
import operator
import heapq
import collections

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
        return self.weight < other.weight


def slow_max_heap():
    gem_num, bag_num = (int(x) for x in read().split())
    gems = [Jewel(*(int(x) for x in read().split())) for _ in range(gem_num)]
    gems.sort(key=operator.attrgetter('value'), reverse=True)
    gems.extend(Jewel(*(int(x) for x in read().split()), 0, True) for _ in range(bag_num))
    gems.sort(key=operator.attrgetter('weight'))
    heap = []
    max_value = 0
    bag_count = 0
    for gem in gems:
        if gem.bag:
            bag_count += 1
            if heap:
                max_value += heapq.heappop(heap)[1].value
        else:
            heapq.heappush(heap, (-gem.value, gem))
        if bag_count == bag_num:
            break
    return max_value


def max_heap():
    # https://www.acmicpc.net/source/19539661 참고
    gem_num, bag_num = (int(x) for x in read().split())
    gems = [tuple(int(x) for x in read().split()) for _ in range(gem_num)]
    gems.sort()
    bags = [int(read().strip()) for _ in range(bag_num)]
    bags.sort()
    heap = []
    max_value = 0
    index = 0
    for bag in bags:
        while index < len(gems):
            weight, value = gems[index]
            if weight > bag:
                if heap:
                    max_value -= heapq.heappop(heap)
                break
            index += 1
            heapq.heappush(heap, -value)
        if index == len(gems):
            max_value -= heapq.heappop(heap)
            if not heap:
                break
    return max_value


def main(mode=''):
    if mode == 'slow_max_heap':
        print(slow_max_heap())
    else:
        print(max_heap())


if __name__ == '__main__':
    main()
