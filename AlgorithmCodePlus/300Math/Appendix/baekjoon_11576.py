# https://www.acmicpc.net/problem/11576
# Solved Date: 20.04.02.

import sys
read = sys.stdin.readline


def new_base(conv_base, decimal):
    if decimal < conv_base:
        return print(decimal, end=' ')
    else:
        value = decimal % conv_base
        new_base(conv_base, decimal // conv_base)
        return print(value, end=' ')


def base_conversion(ori_base, conv_base, num_list):
    decimal = 0
    for index, value in enumerate(num_list):
        decimal += value * (ori_base ** (len(num_list) - index - 1))
    new_base(conv_base, decimal)


def main():
    ori_base, conv_base = (int(x) for x in read().split())
    num_count = int(read().strip())
    num_list = [int(x) for x in read().split()]
    base_conversion(ori_base, conv_base, num_list)


if __name__ == '__main__':
    main()
