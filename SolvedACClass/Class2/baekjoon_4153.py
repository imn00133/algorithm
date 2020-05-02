# https://www.acmicpc.net/problem/4153
# Solved Date: 20.04.07.

import sys
read = sys.stdin.readline


square_save = [x * x for x in range(30000)]


def main():
    while True:
        numbers = [int(x) for x in read().split()]
        if not all(numbers):
            break
        numbers.sort()
        if square_save[numbers[0]] + square_save[numbers[1]] == square_save[numbers[2]]:
            print("right")
        else:
            print("wrong")


if __name__ == '__main__':
    main()
