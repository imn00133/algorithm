# https://www.acmicpc.net/problem/10815
# Solved Date: 20.05.21.

import sys
read = sys.stdin.readline


def search(cards, number):
    left = 0
    right = len(cards) - 1
    while left < right:
        mid = (left + right) // 2
        if cards[mid] < number:
            left = mid + 1
        else:
            right = mid
    if cards[left] == number:
        return '1'
    else:
        return '0'


def binary_search(cards, find_cards):
    ans = []
    for number in find_cards:
        ans.append(search(cards, number))
    return ' '.join(ans)


def hash_map(cards, find_cards):
    ans = []
    for find_num in find_cards:
        if find_num in cards:
            ans.append('1')
        else:
            ans.append('0')
    return ' '.join(ans)


def main(mode=''):
    cards_num = int(read().strip())
    if mode == 'binary':
        cards = sorted([int(x) for x in read().split()])
        find_num = int(read().strip())
        find_cards = [int(x) for x in read().split()]
        print(binary_search(cards, find_cards))
    else:
        cards = set(read().split())
        find_num = int(read().strip())
        find_cards = read().split()
        print(hash_map(cards, find_cards))


if __name__ == '__main__':
    main('binary')
