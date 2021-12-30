# https://www.acmicpc.net/problem/2225
# Solved Date: 20.04.02.
# O(n^2)? https://www.acmicpc.net/source/18848782
# https://do-rang.tistory.com/7 의 방법을 사용하였다.

import sys
read = sys.stdin.readline

MOD = 1000000000
MAX = 200
dp_arr = [[0 for _ in range(MAX+1)] for _ in range(MAX+1)]


def bottom_up(num, k):
    dp_arr[0][0] = 1
    for count in range(1, k+1):
        for number in range(num+1):
            for L in range(number+1):
                dp_arr[count][number] += dp_arr[count-1][number-L]
            dp_arr[count][number] %= MOD


def top_down(num, k):
    pass


def main(mode=''):
    num, k = (int(x) for x in read().split())
    if mode == "top":
        top_down(num, k)
    else:
        bottom_up(num, k)
    print(dp_arr[k][num])


if __name__ == '__main__':
    main()
