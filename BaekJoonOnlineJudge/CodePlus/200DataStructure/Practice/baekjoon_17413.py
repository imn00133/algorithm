# https://www.acmicpc.net/problem/17413
# Solving Date: 20.03.24.
# rev_str의 mode가 'stack'이 되면 stack으로 풀고, 아니면 pythonic하게 해결한다.
# stack사용 시 80ms/pythonic할 경우 64ms가 나온다.

import sys
read = sys.stdin.readline


def all_stack_pop(stack):
    reverse_str = ""
    for _ in range(len(stack)):
        reverse_str += stack.pop()
    return reverse_str


def rev_str(string, mode=''):
    reverse_str = ''
    if mode == 'stack':
        stack = []
        string += '\n'
        for letter in string:
            if letter == ' ':
                reverse_str += all_stack_pop(stack)
                reverse_str += ' '
            elif letter == '\n':
                reverse_str += all_stack_pop(stack)
            else:
                stack.append(letter)
    else:
        rev_list = string.split()
        for word in rev_list:
            reverse_str += word[::-1]
            reverse_str += ' '
        reverse_str = reverse_str.strip()
    return reverse_str


def check_tag(string):
    if string.find('>') == len(string) - 1:
        part_str = ""
        tag = string
    else:
        tag = string[string.find('<'):string.find('>')+1]
        part_str = string[string.find('>')+1:]
    return part_str, tag


def exec_ctrl(string):
    reverse_str = []
    while string:
        # 기저조건 tag가 없을 경우
        if string.find('<') == -1:
            reverse_str.append(rev_str(string, 'stack'))
            string = ""
        elif string[0] == '<':
            string, tag = check_tag(string)
            reverse_str.append(tag)
        else:
            part_str = string[0:string.find('<')]
            string = string[string.find('<'):]
            reverse_str.append(rev_str(part_str, 'stack'))
    print(''.join(reverse_str))


def main(mode=''):
    if mode == 'f':
        file = open("baekjoon_17413_input.txt", mode='r', encoding='utf-8')
        while True:
            string = file.readline().strip()
            if not string:
                break
            exec_ctrl(string)
        file.close()
    else:
        string = read().strip()
        exec_ctrl(string)


if __name__ == '__main__':
    main()
