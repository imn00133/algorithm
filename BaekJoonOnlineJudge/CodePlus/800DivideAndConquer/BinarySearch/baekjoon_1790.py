# https://www.acmicpc.net/problem/1790
# Solved Date: 20.05.13.

import sys
read = sys.stdin.readline


def calc_digit(num):
    digit = 0
    index = 1
    current_multiple = 10 ** index
    prev_multiple = 10 ** (index - 1)
    while num >= current_multiple:
        digit += (current_multiple - prev_multiple) * index
        index += 1
        current_multiple = 10 ** index
        prev_multiple = 10 ** (index - 1)
    digit += (num - prev_multiple + 1) * index
    return digit


def binary_search(num, digit):
    if calc_digit(num) < digit:
        return -1
    left = 1
    right = num
    while left < right:
        mid = (left + right) // 2
        current_digit = calc_digit(mid)
        if current_digit < digit:
            left = mid + 1
        else:
            right = mid
    current_digit = calc_digit(left)
    return str(left)[digit - current_digit - 1]


def main():
    num, digit = (int(x) for x in read().split())
    print(binary_search(num, digit))


if __name__ == '__main__':
    main()
