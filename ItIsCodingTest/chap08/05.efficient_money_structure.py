# 08 다이나믹 프로그래밍 - 효율적인 화폐 구성
# Solved Date: 22.06.23.
import sys
read = sys.stdin.readline

MAX_COUNT = 10001


def dynamic_programming(m, currents):
    dp = [MAX_COUNT for _ in range(m+1)]
    dp[0] = 0
    for current in currents:
        for index in range(current, len(dp)):
            if dp[index-current] != MAX_COUNT:
                dp[index] = min(dp[index], dp[index-current] + 1)
    if dp[-1] == MAX_COUNT:
        return -1
    return dp[-1]


if __name__ == '__main__':
    n, m = (int(x) for x in read().split())
    currents = []
    for _ in range(n):
        currents.append(int(read().rstrip()))
    print(dynamic_programming(m, currents))