# https://www.acmicpc.net/problem/2675
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline


def repeat(repeat_num, string):
    repeat_string = []
    for letter in string:
        repeat_string.append(letter * repeat_num)
    return ''.join(repeat_string)


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        repeat_num, string = read().split()
        print(repeat(int(repeat_num), string))


if __name__ == '__main__':
    main()
