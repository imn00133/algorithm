# https://www.acmicpc.net/problem/1541
# Solved Date: 20.05.19.

import sys
import collections
read = sys.stdin.readline


def slow_solve():
    expression = read().strip()
    change_number_stack = []
    calc_queue = collections.deque()
    sum_number = 0
    for letter in expression:
        if letter in '+-':
            sum_number += int(''.join(change_number_stack))
            change_number_stack.clear()
            if letter == '-':
                calc_queue.append(sum_number)
                sum_number = 0
        else:
            change_number_stack.append(letter)
    sum_number += int(''.join(change_number_stack))
    calc_queue.append(sum_number)

    ans = calc_queue.popleft()
    while calc_queue:
        ans -= calc_queue.popleft()
    return ans


def fast_solve():
    # https://www.acmicpc.net/source/18197192 참고
    expression = read().strip().split('-')
    ans = 0
    for index in range(len(expression)):
        sub_sum = [int(x) for x in expression[index].split('+')]
        if index == 0:
            ans += sum(sub_sum)
        else:
            ans -= sum(sub_sum)
    return ans


def main(mode=''):
    if mode == 'slow':
        ans = slow_solve()
    else:
        ans = fast_solve()
    print(ans)


if __name__ == '__main__':
    main()
