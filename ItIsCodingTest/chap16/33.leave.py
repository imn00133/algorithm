# 16 다이나믹 프로그래밍 - 퇴사
# Solved Date: 22.06.23.
# https://www.acmicpc.net/problem/14501
import sys
read = sys.stdin.readline


# dp: 지속하고 있는 상담이 없을 때 번 돈의 최적해
# 당일 상담을 받고 그 상담이 끝났을 때 번 돈을 상담이 끝난 날로 보냄
# 당일이 되었을 때 오늘과 어제 상담이 없을 때 번 돈의 최적해 확인
# 오늘 받았을 때, 상담이 끝난 날로 번 돈을 보내며, 끝난 날 번 돈의 최적해 확인
def solve():
    days = int(read().rstrip())
    dp = [0 for _ in range(days+1)]
    for index in range(days):
        count_day, pay = (int(x) for x in read().split())

        # 전날과 오늘까지 상담 안 할 때 번 돈의 최적해 확인
        dp[index] = max(dp[index-1], dp[index])

        end_day = index + count_day
        if end_day >= len(dp):
            continue

        dp[end_day] = max(dp[end_day], dp[index] + pay)
    return max(dp[-1], dp[-2])


if __name__ == '__main__':
    print(solve())
