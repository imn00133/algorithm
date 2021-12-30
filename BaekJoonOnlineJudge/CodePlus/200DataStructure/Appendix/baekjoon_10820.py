# https://www.acmicpc.net/problem/10820
# Solving Date: 20.03.28.
# strip()은 공백도 지우기 때문에 명시적으로 '\n'만 지우도록 만든다.
# sys.stdin.readline은 input과 다르게 EOF가 입력되면 빈 string으로 인지한다.
# 이는 sys.stdin이 file과 유사한 객체라고 한다.
# https://cnpnote.tistory.com/에서 [PYTHON]-결말이없는-파이프에서-어떻게-파이썬으로-stdin을-읽는가?를 참고한다.

import sys


def string_count(string):
    division_list = (0, 1, 2, 3)
    lower, upper, num, space = division_list
    count_list = [0 for x in range(len(division_list))]
    for letter in string:
        ascii_num = ord(letter)
        if ord('a') <= ascii_num <= ord('z'):
            count_list[lower] += 1
        elif ord('A') <= ascii_num <= ord('Z'):
            count_list[upper] += 1
        elif ord('0') <= ascii_num <= ord('9'):
            count_list[num] += 1
        else:
            count_list[space] += 1
    return count_list


def main(mode=''):
    read = sys.stdin.readline
    file = None
    if mode == 'f':
        file = open("baekjoon_10820_input.txt", mode='r', encoding='utf-8')
        read = file.readline
    while True:
        string = read().strip('\n')
        if not string:
            if mode == 'f':
                file.close()
            break
        count_list = string_count(string)
        for value in count_list:
            print(value, end=' ')
        print('')


if __name__ == "__main__":
    main()
