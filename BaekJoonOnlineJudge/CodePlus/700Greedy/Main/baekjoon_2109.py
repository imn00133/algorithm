# https://www.acmicpc.net/problem/2109
# Solved Date: 20.05.12.

import sys
import operator
import heapq
read = sys.stdin.readline


def max_heap(requests):
    max_pay = 0
    if not requests:
        return max_pay
    heap = []
    start_day = requests[0][1]
    index = 0
    for current_day in range(start_day, 0, -1):
        while index < len(requests) and requests[index][1] >= current_day:
            heapq.heappush(heap, -requests[index][0])
            index += 1
        if heap:
            max_pay -= heapq.heappop(heap)
    return max_pay


def main():
    request_num = int(read().strip())
    requests = [tuple((int(x) for x in read().split())) for _ in range(request_num)]
    requests.sort(key=operator.itemgetter(1), reverse=True)
    print(max_heap(requests))


if __name__ == '__main__':
    main()

