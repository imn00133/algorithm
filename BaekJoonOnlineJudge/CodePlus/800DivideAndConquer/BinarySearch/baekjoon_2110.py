# https://www.acmicpc.net/problem/2110
# Solved Date: 20.05.14.

import sys
read = sys.stdin.readline


def install_router(houses, length):
    end_install = houses[0]
    count = 1
    for house in houses:
        if end_install + length <= house:
            end_install = house
            count += 1
    return count


def binary_search(houses, router_num):
    left = 1
    right = houses[-1]
    while left < right:
        mid = (left + right) // 2 + 1
        if install_router(houses, mid) >= router_num:
            left = mid
        else:
            right = mid - 1
    return left


def main():
    house_num, router_num = (int(x) for x in read().split())
    house_length = [int(read().strip()) for _ in range(house_num)]
    house_length.sort()
    print(binary_search(house_length, router_num))


if __name__ == '__main__':
    main()
