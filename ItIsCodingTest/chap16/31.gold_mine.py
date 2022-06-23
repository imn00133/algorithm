# 16 다이나믹 프로그래밍 - 금광
# Solved Date: 22.06.23.

import sys
read = sys.stdin.readline

DY = (-1, 0, 1)


def dp_solve(arr):
    # dp[y][x] = x, y 일 때 구한 금의 최적해
    dp = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for y in range(len(arr)):
        dp[y][0] = arr[y][0]

    for x in range(1, len(arr[0])):
        for y in range(len(arr)):
            current_dp = []
            for dy in DY:
                ny = y + dy
                if ny < 0 or ny >= len(arr):
                    continue
                current_dp.append(dp[ny][x-1] + arr[y][x])
            dp[y][x] = max(current_dp)

    answer = 0
    for y in range(len(arr)):
        answer = max(answer, dp[y][-1])
    return answer


def read_testcase():
    n, m = (int(x) for x in read().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    flat_arr = [int(x) for x in read().split()]
    for index, value in enumerate(flat_arr):
        x = index % m
        y = index // m
        arr[y][x] = value
    return arr


def main():
    test_num = int(read().rstrip())
    for _ in range(test_num):
        arr = read_testcase()
        print(dp_solve(arr))


if __name__ == '__main__':
    main()
