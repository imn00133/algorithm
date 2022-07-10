# 17 최단 경로 - 플로이드
# Solved Date: 22.07.10.
# https://www.acmicpc.net/problem/11404
import sys
read = sys.stdin.readline

INT = int(1e9)


def init(arr):
    for i in range(len(arr)):
        arr[i][i] = 0

    bus_num = int(read().rstrip())
    for _ in range(bus_num):
        i, j, cost = (int(x) for x in read().split())
        if cost > arr[i-1][j-1]:
            continue
        arr[i-1][j-1] = cost

    return arr


# 예전에 min이 느렸던 기억이 있는데.
# min 532ms -> 360ms
# conintue는 차이가 있을가? 360ms -> 352ms (이정도면 오차범위)
# https://www.acmicpc.net/source/20438246
def floyd(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                # arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
                cost = arr[i][k] + arr[k][j]
                if arr[i][j] <= cost:
                    continue
                arr[i][j] = cost
    return arr


# print 참고 https://www.acmicpc.net/source/20438246
def arr_print(arr):
    # print 문제인가 해서 확인: 544ms -> 532ms
    # for costs in arr:
    #     print(*[cost if cost != INT else 0 for cost in costs])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == INT:
                arr[i][j] = 0

    for costs in arr:
        print(*costs)


def main():
    city_num = int(read().rstrip())
    arr = [[INT for _ in range(city_num)] for _ in range(city_num)]
    arr = init(arr)
    arr = floyd(arr)
    arr_print(arr)


if __name__ == '__main__':
    main()
