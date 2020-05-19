# https://www.acmicpc.net/problem/1744
# Solved Date: 20.05.19.

import sys
import heapq

read = sys.stdin.readline


def calc_heap(heap):
    calc_value = 0
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        calc_value += num1 * num2
    return calc_value


def main():
    arr_num = int(read().strip())
    negative_heap = []
    positive_heap = []
    zero_exist = False
    one_count = 0
    for _ in range(arr_num):
        number = int(read().strip())
        if number < 0:
            heapq.heappush(negative_heap, number)
        elif number > 1:
            heapq.heappush(positive_heap, -number)
        elif number == 1:
            one_count += 1
        else:
            zero_exist = True

    ans = calc_heap(negative_heap) + calc_heap(positive_heap)
    ans += one_count
    if len(negative_heap) == 1 and not zero_exist:
        ans += negative_heap[0]
    if len(positive_heap) == 1:
        ans += -positive_heap[0]
    print(ans)


if __name__ == '__main__':
    main()
