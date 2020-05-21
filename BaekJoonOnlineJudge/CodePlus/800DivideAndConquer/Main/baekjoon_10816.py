# https://www.acmicpc.net/problem/10816
# Solved Date: 20.05.21.

import sys
import collections
read = sys.stdin.readline


def pythonic(cards):
    return collections.Counter(cards)


def legacy(cards):
    card_counter = collections.defaultdict(int)
    for x in cards:
        card_counter[x] += 1
    return card_counter


def ans_print(card_counter, find_cards):
    for card in find_cards:
        if card in card_counter:
            print(card_counter[card], end=' ')
        else:
            print(0, end=' ')


def fast_ans_print(card_counter, find_cards):
    ans = []
    for card in find_cards:
        if card in card_counter:
            ans.append(f'{card_counter[card]}')
        else:
            ans.append(f'0')
    print(' '.join(ans))


def lower_bound(cards, find_num):
    left = 0
    right = len(cards) - 1
    lower = 0
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == find_num:
            lower = mid
            right = mid - 1
        elif cards[mid] < find_num:
            left = mid + 1
        else:
            right = mid - 1
    return lower


def upper_bound(cards, find_num):
    left = 0
    right = len(cards) - 1
    upper = 0
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == find_num:
            upper = mid + 1
            left = mid + 1
        elif cards[mid] < find_num:
            left = mid + 1
        else:
            right = mid - 1
    return upper


def binary_search(cards, find_cards):
    # python3에서는 시간초과
    ans = []
    for number in find_cards:
        lower = lower_bound(cards, number)
        upper = upper_bound(cards, number)
        ans.append(str(upper - lower))
    return ' '.join(ans)


def main(mode='', counter_mode=''):
    if mode == 'binary':
        card_num = int(read().strip())
        cards = sorted([int(x) for x in read().split()])
        find_card_num = int(read().strip())
        find_cards = [int(x) for x in read().split()]
        print(binary_search(cards, find_cards))
    else:
        card_num = int(read().strip())
        cards = read().split()
        find_card_num = int(read().strip())
        find_cards = read().split()
        if counter_mode == 'legacy':
            card_counter = legacy(cards)
        else:
            card_counter = pythonic(cards)
        fast_ans_print(card_counter, find_cards)


if __name__ == '__main__':
    main('binary')
