# https://www.acmicpc.net/problem/15649
# Solved Date:
# 리스트를 줄여가면서 넘겨주면 더 편할 것 같으나, 메모리를 너무 사용한다.

import sys
read = sys.stdin.readline


def recursion(check, select, n, m):
    if sum(check) == m:
        for num in select:
            print(num, end=' ')
        print()
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        select.append(i+1)
        recursion(check, select, n, m)
        check[i] = False
        select.pop()


def main():
    n, m = (int(x) for x in read().split())
    check = [False for _ in range(n)]
    select = []
    recursion(check, select, n, m)


if __name__ == '__main__':
    main()
