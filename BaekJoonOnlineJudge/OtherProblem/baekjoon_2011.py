# https://www.acmicpc.net/problem/2011
# Solved Date: 20.06.08.

import sys
read = sys.stdin.readline
MAX = 1000000


def is_two_digit(encrypt, index):
    if 0 < int(encrypt[index-1:index+1]) <= 26:
        return True
    else:
        return False


def count_plain_text(encrypt):
    dp_arr = [0 for _ in range(len(encrypt))]
    dp_arr[0] = 1
    if encrypt[1] == '0':
        return 0
    dp_arr[1] = 1
    for index in range(2, len(encrypt)):
        if encrypt[index] != '0':
            dp_arr[index] += dp_arr[index-1]
        if encrypt[index-1] != '0' and is_two_digit(encrypt, index):
            dp_arr[index] += dp_arr[index-2]
        if dp_arr[index] == 0:
            return 0
        dp_arr[index] %= MAX
    return dp_arr[-1]


def main():
    encrypt_text = read().strip()
    encrypt_text = '*' + encrypt_text
    print(count_plain_text(encrypt_text))


if __name__ == '__main__':
    main()
