# https://www.acmicpc.net/problem/15650
# Solved Date: 20.04.07.

import sys
read = sys.stdin.readline


def recursion_order(select, n, m, index=0):
    # 순서를 정함. O(N!)
    if len(select) == m:
        for number in select:
            print(number, end=' ')
        print()
        return
    for i in range(index, n):
        select.append(i+1)
        recursion_order(select, n, m, i+1)
        select.pop()


def recursion(select, n, m, index=0):
    # 선택을 함 O(2^N)
    if len(select) == m:
        for number in select:
            print(number, end=' ')
        print()
        return
    if index >= n:
        return
    select.append(index+1)
    recursion(select, n, m, index+1)
    select.pop()
    recursion(select, n, m, index+1)


def main():
    n, m = (int(x) for x in read().split())
    select = []
    recursion_order(select, n, m)


if __name__ == '__main__':
    main()
