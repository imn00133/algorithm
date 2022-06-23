# 16 다이나믹 프로그래밍 - 못생긴 수
# Solved Date: 22.06.23.

import sys
read = sys.stdin.readline


def solve(n):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    index_2, index_3, index_5 = 0, 0, 0
    next_2, next_3, next_5 = 2, 3, 5
    for index in range(1, n):
        dp[index] = min(next_2, next_3, next_5)
        if next_2 == dp[index]:
            index_2 += 1
            next_2 = dp[index_2] * 2
        if next_3 == dp[index]:
            index_3 += 1
            next_3 = dp[index_3] * 3
        if next_5 == dp[index]:
            index_5 += 1
            next_5 = dp[index_5] * 5
    return dp[n-1]


if __name__ == '__main__':
    n = int(read().rstrip())
    print(solve(n))
