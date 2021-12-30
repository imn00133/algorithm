# https://www.acmicpc.net/problem/11656
# Solving Date: 20.03.29.

import sys
read = sys.stdin.readline


def main():
    string = read().strip()
    postfix_list = []
    for index in range(len(string)):
        postfix_list.append(string[index:])
    postfix_list.sort()
    for postfix in postfix_list:
        print(postfix)


if __name__ == '__main__':
    main()
