# https://www.acmicpc.net/problem/3052
# Solved Date: 20.04.05.

import sys
read = sys.stdin.readline

NUM = 10
MOD = 42


def main():
    # set을 쓰거나 in연산자와 list를 사용할 수 있다.
    remainder = set()
    for _ in range(NUM):
        remainder.add(int(read().strip()) % MOD)
    print(len(remainder))


if __name__ == '__main__':
    main()
