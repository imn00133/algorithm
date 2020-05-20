# https://www.acmicpc.net/problem/12970
# Solved Date: 20.05.20.

import sys
read = sys.stdin.readline


def make_couple(string, couple_num):
    count_a = 0
    count_couple = 0
    for index in range(len(string)):
        current_couple = count_couple + (len(string) - index - 1) - count_a
        if current_couple <= couple_num:
            string[index] = 'A'
            count_a += 1
            count_couple = current_couple
            if count_couple == couple_num:
                return ''.join(string)
    return -1


def main():
    string_num, couple_num = (int(x) for x in read().split())
    string = ['B' for _ in range(string_num)]
    print(make_couple(string, couple_num))


if __name__ == '__main__':
    main()
