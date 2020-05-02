# https://www.acmicpc.net/problem/1932
# Solved Date: 20.04.06.
# bottom_up을 아래서 위로 더해갈 수도 있다.
# https://www.acmicpc.net/source/18902254

import sys
read = sys.stdin.readline


MAX = 500
dp_arr = [[0 for _ in range(MAX)] for _ in range(MAX)]


def bottom_up(triangle):
    dp_arr[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for k in range(len(triangle[i])):
            if k == 0:
                dp_arr[i][k] = dp_arr[i-1][k] + triangle[i][k]
            elif k == len(triangle[i])-1:
                dp_arr[i][k] = dp_arr[i-1][k-1] + triangle[i][k]
            else:
                dp_arr[i][k] = max(dp_arr[i-1][k-1], dp_arr[i-1][k]) + triangle[i][k]


def top_down(triangle):
    pass


def main(mode=''):
    size = int(read().strip())
    triangle = []
    for _ in range(size):
        triangle.append([int(x) for x in read().split()])
    if mode == 'top':
        top_down(triangle)
    else:
        bottom_up(triangle)
    print(max(dp_arr[size-1]))


if __name__ == '__main__':
    main()
