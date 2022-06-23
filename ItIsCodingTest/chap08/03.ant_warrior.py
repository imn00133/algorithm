# 08 다이나믹 프로그래밍 - 개미 전사
# Solved Date: 22.05.18.
import sys

read = sys.stdin.readline


def dynamic_programming_in_book(warehouse):
    dp = [0 for _ in range(len(warehouse))]
    dp[0] = warehouse[0]
    dp[1] = max(warehouse[0], warehouse[1])
    for index in range(2, len(warehouse)):
        dp[index] = max(dp[index-1], dp[index-2] + warehouse[index])
    return dp[-1]


# 100 1 2 100
# i-1은 선택할 수 없음 = i-3까지 불가, i-2는 선택 가능 하기 때문에 i-3이 최대일 경우가 존재하여, i-3까지 확인해야 함
# i-1, i-2만 확인하면 다 확인할 수 있다고 주장
# i-1 을 선택하면 => i 선택하지 않는다
# i-2를 선택하면  => i를 선택한다.
# i-2가 최적해가 보장되어있다.
# 최적해가 무엇인가 -> 잘 만드는게 중요하고
# dp[i][0] = 0...i번째 신량창고중에서 선택을해 - i번째를 털었을 때의 최적해
# dp[i][1] = i번째를 털지 않았을 때 최적해
# dp[i][0] = dp[i-1][1] + food[i]
# dp[i][1] = max(dp[i-1][0..1])
def dynamic_programming(warehouse):
    dp = [0 for _ in range(len(warehouse))]
    dp[0] = warehouse[0]
    dp[1] = warehouse[1]
    dp[2] = warehouse[0] + warehouse[2]
    for index in range(3, len(warehouse)):
        dp[index] = max(dp[index-1], dp[index-2] + warehouse[index], dp[index-3] + warehouse[index])
    return dp[-1]


def main():
    warehouse_count = int(read().rstrip())
    warehouse = [int(x) for x in read().split()]
    print(dynamic_programming(warehouse))


if __name__ == '__main__':
    main()
