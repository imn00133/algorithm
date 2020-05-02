# https://www.acmicpc.net/problem/15829
# Solved Date: 20.05.02.

import sys
read = sys.stdin.readline


def main():
    str_num = read()
    string = read().strip()
    r = 31
    M = 1234567891
    hash_value = 0
    for index in range(len(string)):
        letter_value = ord(string[index]) - ord('a') + 1
        hash_value += (letter_value * (r ** index)) % M
    print(hash_value % M)


if __name__ == '__main__':
    main()
