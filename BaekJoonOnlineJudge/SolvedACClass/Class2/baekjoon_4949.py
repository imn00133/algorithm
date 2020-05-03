# https://www.acmicpc.net/problem/4949
# Solved Date: 20.05.03.
# https://www.acmicpc.net/source/14057717를 참고해 코드를 간추림

import sys
read = sys.stdin.readline


def error_check_stack(stack, check_value):
    if not stack:
        return True
    elif stack.pop() != check_value:
        return True
    return False


def solve(sentence):
    stack = []
    for letter in sentence:
        if letter in '([':
            stack.append(letter)
        elif letter == ')' and error_check_stack(stack, '('):
            return "no"
        elif letter == ']' and error_check_stack(stack, '['):
            return "no"
    if not stack:
        return "yes"
    else:
        return "no"


def main():
    while True:
        sentence = read().rstrip()
        if sentence == '.':
            break
        print(solve(sentence))


if __name__ == '__main__':
    main()
