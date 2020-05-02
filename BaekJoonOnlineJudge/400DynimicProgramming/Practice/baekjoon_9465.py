# https://www.acmicpc.net/problem/9465
# Solved Date: 20.04.05.

import sys
sys.setrecursionlimit(10 ** 4)


def bottom_up(sticker_num, sticker, dp_arr):
    # 0 위, 1 아래, 2 없음
    # 없을 경우가 연속되면, 값이 커질 수 없어 계산하지 않음
    dp_arr[0][0] = sticker[0][0]
    dp_arr[0][1] = sticker[1][0]
    dp_arr[0][2] = 0
    for i in range(1, sticker_num):
        # sticker를 각각 더하지 않고, max를 구한 후, 더하는게 더 좋다.
        dp_arr[i][0] = max(dp_arr[i-1][1], dp_arr[i-1][2]) + sticker[0][i]
        dp_arr[i][1] = max(dp_arr[i-1][0], dp_arr[i-1][2]) + sticker[1][i]
        dp_arr[i][2] = max(dp_arr[i-1][0], dp_arr[i-1][1])
    return dp_arr


def top_down(i, sticker, dp_arr):
    # 시간초과...
    if i == 0:
        dp_arr[i][0] = sticker[0][i]
        dp_arr[i][1] = sticker[1][i]
        dp_arr[i][2] = 0
        return dp_arr[i]
    if all(dp_arr[i]):
        return dp_arr[i]
    dp_arr[i][0] = max(top_down(i-1, sticker, dp_arr)[1], top_down(i-1, sticker, dp_arr)[2]) + sticker[0][i]
    dp_arr[i][1] = max(top_down(i-1, sticker, dp_arr)[0], top_down(i-1, sticker, dp_arr)[2]) + sticker[1][i]
    dp_arr[i][2] = max(top_down(i-1, sticker, dp_arr)[0], top_down(i-1, sticker, dp_arr)[1])
    return dp_arr[i]


def main(mode='', file=''):
    read = sys.stdin.readline
    if file:
        file = open("baekjoon_9465_input.txt", mode='r', encoding='utf-8')
        read = file.readline
    test_case_num = int(read().strip())
    for test_case in range(test_case_num):
        sticker_num = int(read().strip())
        dp_arr = [[0 for _ in range(3)] for _ in range(sticker_num)]
        sticker = []
        for _ in range(2):
            sticker.append([int(x) for x in read().split()])
        if mode == 'top':
            if sticker_num > 2000:
                for part_num in range(2000, sticker_num-1, 2000):
                    top_down(part_num, sticker, dp_arr)
            # 같은 방식으로 받아주는게 좋으나, 되돌려주려면 함수를 하나 더 만들어야 한다. 없어도 가능
            top_down(sticker_num-1, sticker, dp_arr)
        else:
            dp_arr = bottom_up(sticker_num, sticker, dp_arr)
        print(max(dp_arr[sticker_num-1]))
    if file:
        file.close()


if __name__ == '__main__':
    main()
