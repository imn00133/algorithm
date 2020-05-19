# https://www.acmicpc.net/problem/16198
# Solved Date: 20.05.19.

import sys
read = sys.stdin.readline


def recursion(marbles, partial_sum=0):
    if len(marbles) == 2:
        return partial_sum
    max_sum = 0
    for index in range(1, len(marbles) - 1):
        number = marbles.pop(index)
        value = recursion(marbles, partial_sum + marbles[index - 1] * marbles[index])
        if value > max_sum:
            max_sum = value
        marbles.insert(index, number)
    return max_sum


def fast_recursion(marbles, partial_sum=0):
    # https://www.acmicpc.net/source/17793412 참고
    if len(marbles) == 2:
        return partial_sum
    max_sum = 0
    for index in range(1, len(marbles) - 1):
        value = recursion(marbles[:index] + marbles[index+1:], partial_sum + marbles[index-1] * marbles[index+1])
        if value > max_sum:
            max_sum = value
    return max_sum


def main(mode=''):
    marble_num = int(read().strip())
    marbles = [int(x) for x in read().split()]
    if mode == 'fast':
        print(fast_recursion(marbles))
    else:
        print(recursion(marbles))


if __name__ == '__main__':
    main('fast')
