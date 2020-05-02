# https://www.acmicpc.net/problem/10816
# Solved Date: 20.05.02.

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


def main(mode='pythonic'):
    card_num = int(read().strip())
    cards = read().split()
    if mode == 'pythonic':
        card_counter = pythonic(cards)
    else:
        card_counter = legacy(cards)
    find_card_num = int(read().strip())
    find_cards = read().split()
    fast_ans_print(card_counter, find_cards)


if __name__ == '__main__':
    main('pythonic')
