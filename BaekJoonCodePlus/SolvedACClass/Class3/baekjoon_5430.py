# https://www.acmicpc.net/problem/5430
# Solved Date: 20.05.02.
# https://www.acmicpc.net/source/17199517 참고

import sys
import collections

read = sys.stdin.readline


def calculate(operations, arr):
    if operations.count('D') > len(arr):
        return 'error'
    right_pop = False
    for op in operations:
        if op == 'R':
            right_pop = not right_pop
        elif right_pop:
            arr.pop()
        else:
            arr.popleft()
    if right_pop:
        arr.reverse()
    return '[' + ','.join(arr) + ']'


def use_deck():
    test_num = int(read().strip())
    for _ in range(test_num):
        operations = read().strip()
        arr_num = int(read().strip())
        arr = collections.deque(read()[1:-2].split(','))
        if arr_num == 0:
            arr = []
        print(calculate(operations, arr))


def operation(operations, arr_num):
    start = 0
    end = arr_num
    forward = True
    for op in operations:
        if op == "D":
            if forward:
                start += 1
            else:
                end -= 1
        else:
            forward = not forward
    return start, end, forward


def op_calculate():
    test_num = int(read().strip())
    for _ in range(test_num):
        operations = read().strip()
        arr_num = int(read().strip())
        start, end, forward = operation(operations, arr_num)
        if start > end:
            arr = read()
            print('error')
        else:
            if forward:
                arr = read()[1:-2].split(',')[start:end]
            else:
                arr = read()[1:-2].split(',')[start:end]
                arr.reverse()
            print('['+','.join(arr)+']')


def main(mode=''):
    if mode == 'deck':
        use_deck()
    else:
        op_calculate()


if __name__ == '__main__':
    main()
