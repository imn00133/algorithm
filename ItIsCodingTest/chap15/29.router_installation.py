# 15 이진 탐색 - 공유기 설치
# Solved Date: 22.05.14.
# https://www.acmicpc.net/problem/2110
import sys
read = sys.stdin.readline


def install_router(arr, router_num, install_length):
    install_num = 1
    prev_install_pos = arr[0]
    for house_pos in arr:
        if house_pos >= prev_install_pos + install_length:
            install_num += 1
            prev_install_pos = house_pos
        # early return 확인이 훨씬 느림
        # if install_num == router_num:
        #     return True
    return install_num >= router_num


def binary_exploration(arr, router_num):
    left, right = 0, arr[-1]
    while left < right:
        mid = (left + right) // 2 + 1
        if install_router(arr, router_num, mid):
            left = mid
        else:
            right = mid - 1
    return left


def main():
    arr_num, router_num = [int(x) for x in read().split()]
    arr = [0 for _ in range(arr_num)]
    for index in range(arr_num):
        arr[index] = int(read().rstrip())
    print(binary_exploration(sorted(arr), router_num))


if __name__ == '__main__':
    main()
