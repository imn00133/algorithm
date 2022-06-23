# 08 다이나믹 프로그래밍 - 바닥 공사
# Solved Date: 22.06.23.


def dynamic_programming(num):
    dp = [0 for _ in range(num)]
    dp[0] = 1
    dp[1] = 3
    for index in range(2, num):
        dp[index] = dp[index-1] + 2 * dp[index-2]
    return dp[num-1]


if __name__ == '__main__':
    num = int(input())
    print(dynamic_programming(num) % 796796)
