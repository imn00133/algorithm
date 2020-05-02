# https://www.acmicpc.net/problem/1259
# Solved Date: 20.04.12.

import sys
read = sys.stdin.readline


def check_palindrome(num):
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            return False
    return True


def main():
    while True:
        num = read().strip()
        if num == '0':
            break
        if check_palindrome(num):
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
