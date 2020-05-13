# https://www.acmicpc.net/problem/1654
# Solved Date: 20.05.13.

import sys
read = sys.stdin.readline


def cutting_wire(length, wires):
    count = 0
    for wire in wires:
        count += wire // length
    return count


def binary_search(need_num, wires):
    left = 0
    right = max(wires)
    while left < right:
        mid = (left + right) // 2 + 1
        if need_num <= cutting_wire(mid, wires):
            left = mid
        else:
            right = mid - 1
    return left


def main():
    wire_num, need_num = (int(x) for x in read().split())
    wires = [int(read().strip()) for _ in range(wire_num)]
    print(binary_search(need_num, wires))


if __name__ == '__main__':
    main()
