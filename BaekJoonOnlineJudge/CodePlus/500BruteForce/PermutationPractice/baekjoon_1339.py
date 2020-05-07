# https://www.acmicpc.net/problem/1339
# Solved Date:

import sys
import collections
import itertools

read = sys.stdin.readline


def digit_change(calc_num):
    for index in range(len(calc_num) - 1, 0, -1):
        calc_num[index-1] += calc_num[index] // 10
        calc_num[index] %= 10
    return int(''.join([str(x) for x in calc_num]))


def calc(letter_index, max_len):
    keys = letter_index.keys()
    nums = tuple([x for x in range(9, 9 - len(keys), -1)])
    max_num = 0
    for select_nums in itertools.permutations(nums):
        calc_num = [0 for _ in range(max_len + 1)]
        for letter, number in zip(keys, select_nums):
            for index in letter_index[letter]:
                calc_num[index] += number
        calc_value = digit_change(calc_num)
        if max_num < calc_value:
            max_num = calc_value
    return max_num


def pre_process_word(letter_index, word):
    for index in range(len(word)):
        letter = word[index]
        letter_index[letter].append(-(len(word) - index))
    return letter_index


def permutation():
    # python으로는 시간초과, pypy3로도 6000s정도 걸린다.
    word_num = int(read().strip())
    letter_index = collections.defaultdict(list)
    max_len = 0
    for _ in range(word_num):
        word = read().strip()
        letter_index = pre_process_word(letter_index, word)
        max_len = max(len(word), max_len)
    print(calc(letter_index, max_len))


def assign_number(letter_digit):
    ans = 0
    nums = sorted(list(letter_digit.values()), reverse=True)
    index = range(9, 9 - len(nums), -1)
    for number, i in zip(nums, index):
        ans += number * i
    return ans


def pre_process(letter_digit, word):
    for index in range(len(word)):
        letter = word[index]
        digit = len(word) - index - 1
        letter_digit[letter] += 10 ** digit
    return letter_digit


def mathematics():
    word_num = int(read().strip())
    letter_digit = collections.defaultdict(int)
    for _ in range(word_num):
        word = read().strip()
        letter_digit = pre_process(letter_digit, word)
    print(assign_number(letter_digit))


def main(mode=''):
    if mode == 'permutation':
        permutation()
    else:
        mathematics()


if __name__ == '__main__':
    main()
