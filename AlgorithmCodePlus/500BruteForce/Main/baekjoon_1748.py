# https://www.acmicpc.net/problem/1748
# Solved Date: 20.04.06.

import sys
read = sys.stdin.readline

DIGIT = [10 ** x for x in range(9)]


def brute_force(num):
    num_digit = len(str(num))
    new_num_digit = 0
    for digit in range(1, num_digit):
        new_num_digit += digit * (DIGIT[digit] - DIGIT[digit-1])
    new_num_digit += num_digit * (num - DIGIT[num_digit-1] + 1)
    return new_num_digit


def main():
    num = int(read().strip())
    print(brute_force(num))


if __name__ == '__main__':
    main()
