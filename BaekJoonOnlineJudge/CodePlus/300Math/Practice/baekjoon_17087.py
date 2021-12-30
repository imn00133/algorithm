# https://www.acmicpc.net/problem/17087
# Solving Date: 20.03.29.
# N이 10^5여서 stack이 터지는 듯 하다. 재귀는 불가능한 것으로 판단.

import sys


def gcd(num1, num2):
    while num2:
        r = num1 % num2
        num1, num2 = num2, r
    return num1


def calc_all_gcd(children_rel_pos):
    all_gcd = children_rel_pos[0]
    for position in children_rel_pos[1:]:
        all_gcd = gcd(all_gcd, position)
        if all_gcd == 1:
            break
    return all_gcd


def main(mode=''):
    read = sys.stdin.readline
    file = None
    if mode == 'f':
        file = open('baekjoon_17087_input3.txt', mode='r', encoding='utf-8')
        read = file.readline

    children_num, me_pos = (int(x) for x in read().split())
    children_pos = [int(x) for x in read().split()]
    children_relative_pos = [abs(x - me_pos) for x in children_pos]
    all_gcd = calc_all_gcd(children_relative_pos)
    print(all_gcd)

    if mode == 'f':
        file.close()


if __name__ == '__main__':
    main()
