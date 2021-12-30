# https://www.acmicpc.net/problem/16194
# Solved Date: 20.03.31.
# top_down은 https://takeknowledge.tistory.com/104의 도움을 받았다.

import sys
sys.setrecursionlimit(10 ** 4)
read = sys.stdin.readline

MAX = 1000
dp_arr = [-1 for _ in range(MAX + 1)]


def bottom_up(num, card_pack):
    dp_arr[0] = 0
    for index in range(1, num+1):
        for j in range(1, index+1):
            if dp_arr[index] == -1 or dp_arr[index] > dp_arr[index-j] + card_pack[j]:
                dp_arr[index] = dp_arr[index-j] + card_pack[j]
    return dp_arr[num]


def top_down(num, card_pack):
    # 이걸 재귀로 풀 수 있는 걸까?
    if num == 0:
        dp_arr[num] = card_pack[num]
        return dp_arr[num]
    if dp_arr[num] > -1:
        return dp_arr[num]
    for index in range(1, num+1):
        if dp_arr[num] == -1 or dp_arr[num] > top_down(num-index, card_pack) + card_pack[index]:
            dp_arr[num] = top_down(num-index, card_pack) + card_pack[index]
    return dp_arr[num]


def main(mode=''):
    purchase_num = int(read().strip())
    card_pack = [0]
    temp_pack = read().split()
    card_pack.extend([int(x) for x in temp_pack])
    if mode == 'top':
        print(top_down(purchase_num, card_pack))
    else:
        print(bottom_up(purchase_num, card_pack))


if __name__ == '__main__':
    main('top')
