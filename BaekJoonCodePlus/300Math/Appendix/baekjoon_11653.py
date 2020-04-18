# https://www.acmicpc.net/problem/11653
# Sovled Date: 20.04.02.

import sys
read = sys.stdin.readline


def prime_factorization(num):
    temp = num
    for number in range(2, num):
        if temp == 0 or number ** 2 > num:
            break
        while temp % number == 0:
            temp //= number
            print(number)
    # 모든 소수를 점검하지 않았으나, 남는 수는 소수이다.
    if temp != 1:
        print(temp)


def main():
    num = int(read().strip())
    prime_factorization(num)


if __name__ == "__main__":
    main()
