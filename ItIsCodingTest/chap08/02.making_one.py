# 08 다이나믹 프로그래밍 - 1로 만들기
# Solved Date: 22.05.18.
import sys

read = sys.stdin.readline


def dynamic_programming(num):
    dp = [0 for _ in range(num + 1)]
    for index in range(2, num + 1):
        dp[index] = dp[index-1] + 1
        if index % 2 == 0:
            dp[index] = min(dp[index], dp[index//2] + 1)
        if index % 3 == 0:
            dp[index] = min(dp[index], dp[index//3] + 1)
        if index % 5 == 0:
            dp[index] = min(dp[index], dp[index//5] + 1)
    return dp[num]


def main():
    num = int(read().rstrip())
    print(dynamic_programming(num))


if __name__ == '__main__':
    main()
