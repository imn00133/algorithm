# https://www.acmicpc.net/problem/9019
# Solved Date: 20.05.29.

import sys
import collections

read = sys.stdin.readline
MAX = 10 ** 4


def operation(op, number):
    # https://www.acmicpc.net/source/15672693 참고
    if op == 0:
        return (number * 2) % MAX, 'D'
    elif op == 1:
        return (number + MAX - 1) % MAX, 'S'
    elif op == 2:
        return (number % 1000) * 10 + (number // 1000), 'L'
    else:
        return (number % 10) * 1000 + (number // 10), 'R'


def explorer(start, end):
    visit = ['' for _ in range(MAX + 1)]
    queue = collections.deque()
    if start == end:
        return ''
    visit[start] = ' '
    queue.append(start)
    while queue:
        number = queue.popleft()
        for op in range(4):
            new_num, letter = operation(op, number)
            if visit[new_num]:
                continue
            if new_num == end:
                return (visit[number] + letter).strip()
            visit[new_num] = visit[number] + letter
            queue.append(new_num)


def main():
    test_case = int(read().strip())
    for _ in range(test_case):
        start, end = (int(x) for x in read().split())
        print(explorer(start, end))


if __name__ == '__main__':
    main()
