# https://www.acmicpc.net/problem/1003
# Solved Date: 20.05.03.

import sys
read = sys.stdin.readline

MAX = 40
dp_arr = [[-1, -1] for _ in range(MAX + 1)]


def top_down(number):
    if number == 0:
        dp_arr[0][0] = 1
        dp_arr[0][1] = 0
        return dp_arr[0]
    elif number == 1:
        dp_arr[1][0] = 0
        dp_arr[1][1] = 1
        return dp_arr[1]
    if dp_arr[number][0] > 0:
        return dp_arr[number]
    index = 0
    for num1, num2 in zip(top_down(number - 1), top_down(number - 2)):
        dp_arr[number][index] = num1 + num2
        index += 1
    return dp_arr[number]


def main():
    test_case = int(read().strip())
    for _ in range(test_case):
        fibonacci_num = int(read().strip())
        print(*top_down(fibonacci_num))


if __name__ == '__main__':
    main()
