# 14 정렬 - 실패율
# Solved Date: 22.04.13.
# https://programmers.co.kr/learn/courses/30/lessons/42889
import sys
import heapq

read = sys.stdin.readline


# 문제를 풀고 arr를 받지 않고, 바로 heap으로 넣는게 빠르다는 점을 알게 됨
# 참고 https://www.acmicpc.net/source/26650179
# 이렇게 바꿔도 시간의 차이는 없다?
def min_heap():
    arr_num = int(read().rstrip())
    heap = []

    for _ in range(arr_num):
        heapq.heappush(heap, int(read().rstrip()))

    total_comparison = 0
    # 이렇게 하는게 좀 더 간편함
    # while True -> if len(heap) == 1 로 빠져나는 것보다 약간 빠름(212 -> 204ms)
    while len(heap) >= 2:
        partial_sum = heapq.heappop(heap) + heapq.heappop(heap)
        total_comparison += partial_sum
        heapq.heappush(heap, partial_sum)
    return total_comparison


# time out
def insert_sort():
    arr_num = int(read().rstrip())
    arr = [int(read().rstrip()) for _ in range(arr_num)]

    sort_arr = sorted(arr, reverse=True)
    total_comparison = 0
    while True:
        if len(sort_arr) == 1:
            return total_comparison
        sort_arr.append(sort_arr.pop() + sort_arr.pop())
        total_comparison += sort_arr[-1]
        for index in range(1, len(sort_arr)):
            if sort_arr[-index] > sort_arr[-(index+1)]:
                sort_arr[-index], sort_arr[-(index+1)] = sort_arr[-(index+1)], sort_arr[-index]
            else:
                break


# 직관적으로 두 개씩 더 할 때 가장 작은 값을 더해야 작음
# 이 값이 다시 들어가서 더해지는 구조
# a, b, c => 2*(a+b) + c / 2*(b+c) + a
# 삽입정렬을 통해 문제 풀이
# 최소힙을 사용하면 편할 거 같은데..?
def main():
    print(min_heap())


if __name__ == '__main__':
    main()
