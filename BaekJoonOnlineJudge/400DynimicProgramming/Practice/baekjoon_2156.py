# https://www.acmicpc.net/problem/2156
# Solved Date:

import sys
read = sys.stdin.readline

MAX = 10000
dp_arr = [[0 for _ in range(3)] for _ in range(MAX+1)]


def one_bottom_up(wines):
    dp_arr[0][0] = wines[0]
    dp_arr[1][0] = wines[0] + wines[1]
    for i in range(2, len(wines)):
        dp_arr[i][0] = max(dp_arr[i-1][0], dp_arr[i-2][0] + wines[i], dp_arr[i-3][0] + wines[i] + wines[i-1])


def bottom_up(wines):
    dp_arr[0][1] = wines[0]
    for i in range(1, len(wines)):
        dp_arr[i][0] = max(dp_arr[i-1])
        dp_arr[i][1] = dp_arr[i-1][0] + wines[i]
        dp_arr[i][2] = dp_arr[i-1][1] + wines[i]


def top_down(wines, index):
    pass


def main(mode=''):
    wine_num = int(read().strip())
    wines = []
    for _ in range(wine_num):
        wines.append(int(read().strip()))
    if mode == 'top':
        top_down(wines, len(wines)-1)
    elif mode == 'one':
        one_bottom_up(wines)
    else:
        bottom_up(wines)
    print(max(dp_arr[wine_num-1]))


if __name__ == '__main__':
    main('one')
