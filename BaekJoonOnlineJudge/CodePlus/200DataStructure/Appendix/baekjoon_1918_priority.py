# https://www.acmicpc.net/problem/1918
# Solving Date: 20.03.27.

import sys


def priority(operator):
    if operator == '(':
        return 0
    elif operator in '+-':
        return 1
    else:
        return 2


def convert_postfix(expression):
    postfix_expression = []
    operator_stack = []
    for value in expression:
        if ord('A') <= ord(value) <= ord('Z'):
            postfix_expression.append(value)
        # 기저조건: 비어있거나, (를 만났을 때
        elif not operator_stack or value == '(':
            operator_stack.append(value)
        elif value == ')':
            while operator_stack[-1] != '(':
                postfix_expression.append(operator_stack.pop())
            # '('를 제거
            operator_stack.pop()
        else:
            # stack내 연산자의 우선순위가 크거나 같으면 pop함
            while operator_stack and priority(operator_stack[-1]) >= priority(value):
                postfix_expression.append(operator_stack.pop())
            operator_stack.append(value)
    while operator_stack:
        postfix_expression.append(operator_stack.pop())
    postfix_expression = ''.join(postfix_expression)
    return postfix_expression


def main(mode=''):
    read = sys.stdin.readline
    file = None
    if mode == 'f':
        file = open("baekjoon_1918_input.txt", mode='r', encoding='utf-8')
        read = file.readline
    expression = list(read().strip())
    print(convert_postfix(expression))
    if mode == 'f':
        file.close()


if __name__ == '__main__':
    main()
