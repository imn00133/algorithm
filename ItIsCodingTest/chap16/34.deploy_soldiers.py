# 16 다이나믹 프로그래밍 - 병사 배치하기
# Solved Date: 22.07.03.
# https://www.acmicpc.net/problem/18353
import sys
read = sys.stdin.readline


# 간만에 다시 봄
def dynamic_programming(soldiers):
    # DP[i]는 A[1] ... A[i]까지 가장 길게 감소하는 수열
    dp = [0 for _ in range(len(soldiers))]
    for current_index, soldier in enumerate(soldiers):
        for prev_index in range(current_index):
            if soldiers[prev_index] <= soldier:
                continue
            dp[current_index] = max(dp[current_index], dp[prev_index] + 1)
    return len(soldiers) - max(dp) - 1


def main():
    _ = int(read().rstrip())
    soldiers = [int(x) for x in read().split()]
    print(dynamic_programming(soldiers))


if __name__ == '__main__':
    main()
