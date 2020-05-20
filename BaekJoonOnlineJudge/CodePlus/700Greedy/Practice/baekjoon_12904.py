# https://www.acmicpc.net/problem/12904
# Solved Date: 20.05.20.

import sys
read = sys.stdin.readline


def is_same_string(original, answer, start_pointer, end_pointer, end_flag):
    if end_flag:
        return original == answer[start_pointer:end_pointer]
    else:
        return original == ''.join(reversed(answer[start_pointer:end_pointer]))


def greedy(original, answer):
    start_pointer = 0
    end_pointer = len(answer) - 1
    end_flag = True
    while end_pointer - start_pointer + 1 > len(original):
        if end_flag:
            if answer[end_pointer] == 'B':
                end_flag = not end_flag
            end_pointer -= 1
        else:
            if answer[start_pointer] == 'B':
                end_flag = not end_flag
            start_pointer += 1
    if is_same_string(original, answer, start_pointer, end_pointer + 1, end_flag):
        return 1
    else:
        return 0


def main():
    original = read().strip()
    answer = read().strip()
    print(greedy(original, answer))


if __name__ == '__main__':
    main()
