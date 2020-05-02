# https://www.acmicpc.net/problem/1920
# Solved Date: 20.05.02.

import sys
read = sys.stdin.readline


def main():
    input_num = read().strip()
    input_set = set(read().split())
    question_num = read().strip()
    ans = []
    for number in read().split():
        if number in input_set:
            ans.append(f'1\n')
        else:
            ans.append(f'0\n')
    print(''.join(ans))


if __name__ == '__main__':
    main()
