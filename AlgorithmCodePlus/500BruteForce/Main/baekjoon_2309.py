# https://www.acmicpc.net/problem/2309
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline

DWARF_NUM = 9


def solve(dwarfs):
    total = sum(dwarfs)
    for i in range(DWARF_NUM):
        for j in range(i+1, DWARF_NUM):
            if total - dwarfs[i] - dwarfs[j] == 100:
                dwarfs.pop(i)
                dwarfs.pop(j-1)
                return dwarfs


def main():
    dwarfs = []
    for _ in range(DWARF_NUM):
        dwarfs.append(int(read().strip()))
    real_dwarfs = solve(dwarfs)
    real_dwarfs.sort()
    for value in real_dwarfs:
        print(value)


if __name__ == '__main__':
    main()
