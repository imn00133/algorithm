# https://www.acmicpc.net/problem/2908
# Solved Date: 20.04.04.
# 문자열을 뒤집을 때, [::-1]을 까먹지 말자.
# 문자열끼리도 비교가 된다.
# https://www.acmicpc.net/source/18912988


import sys
read = sys.stdin.readline


def main():
    nums = [reversed(list(s)) for s in read().split()]
    nums = [int(''.join(s)) for s in nums]
    print(max(nums))


if __name__ == '__main__':
    main()
