# 16 다이나믹 프로그래밍 - 정수 삼각형
# Solved Date: 22.07.03.
# https://www.acmicpc.net/problem/1932
import sys
read = sys.stdin.readline


# 역순으로 하면 빠를까 싶지 않았는데, 결국 초기화 과정이 있어서 같음
def solve():
    triangle_size = int(read().rstrip())

    # index까지 내려온 덧셈 최대 값
    dp = [[0 for _ in range(triangle_size)] for _ in range(triangle_size)]
    for line_index in range(triangle_size):
        line = [int(x) for x in read().split()]
        for index, value in enumerate(line):
            if index == 0:
                dp[line_index][index] = dp[line_index-1][index] + value
                continue
            dp[line_index][index] = max(dp[line_index-1][index-1], dp[line_index-1][index]) + value
    return max(dp[-1])


if __name__ == '__main__':
    print(solve())
