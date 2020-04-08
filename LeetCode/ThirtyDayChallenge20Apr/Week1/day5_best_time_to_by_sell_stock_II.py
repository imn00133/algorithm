# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# Solved Date: 20.04.05.
# 속도는 비슷하다.


def another_profit(prices):
    # Simple One Pass
    profit = 0
    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            profit += prices[i] - prices[i-1]
    return profit


def max_profit(prices):
    # Peak Valley Approach
    profit = 0
    buy_value = -1
    for i in range(len(prices)):
        if i == len(prices) - 1:
            if buy_value != -1:
                profit += prices[i] - buy_value
        elif buy_value == -1 and prices[i] < prices[i+1]:
            buy_value = prices[i]
        elif buy_value != -1 and prices[i] > prices[i+1]:
            profit += prices[i] - buy_value
            buy_value = -1
    return profit


def main():
    prices = [int(x) for x in input().split()]
    print(another_profit(prices))
    print(max_profit(prices))


if __name__ == '__main__':
    main()
