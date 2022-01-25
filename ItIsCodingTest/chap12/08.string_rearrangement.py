# chap08 구현 - 문자열 재정렬
# Solved Date: 22.01.26.

import sys

read = sys.stdin.readline


def solve(string):
    answer = []
    number_sum = 0
    for character in string:
        if character.isalpha():
            answer.append(character)
        else:
            number_sum += int(character)
    answer.sort()
    return ''.join(answer) + str(number_sum)


if __name__ == '__main__':
    string = list(read().rstrip())
    print(solve(string))
