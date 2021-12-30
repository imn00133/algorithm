# https://www.acmicpc.net/problem/10818
# Solving Date: 20.03.29.

import sys
read = sys.stdin.readline


def legacy(num_list):
    max_num = min_num = num_list[0]
    for number in num_list:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
    return max_num, min_num


def pythonic(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return max_num, min_num


def main():
    num_count = int(read().strip())
    num_list = [int(x) for x in read().split()]
    max_num, min_num = legacy(num_list)
    print(min_num, max_num)


if __name__ == '__main__':
    main()
