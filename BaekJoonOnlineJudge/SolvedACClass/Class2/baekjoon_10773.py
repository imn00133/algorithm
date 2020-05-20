# https://www.acmicpc.net/problem/10773
# Solved Dated: 20.05.20.

import sys
read = sys.stdin.readline


def main():
    number_count = int(read().strip())
    stack = []
    for _ in range(number_count):
        number = int(read().strip())
        if number > 0:
            stack.append(number)
        else:
            stack.pop()
    print(sum(stack))


if __name__ == '__main__':
    main()
