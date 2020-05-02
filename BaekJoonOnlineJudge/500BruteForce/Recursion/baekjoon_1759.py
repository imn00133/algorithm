# https://www.acmicpc.net/problem/1759
# Solved Date: 20.04.16.

import sys
read = sys.stdin.readline

VOWELS = ('a', 'e', 'i', 'o', 'u')


def validation(ans):
    vowel_num = 0
    for vowel in VOWELS:
        if vowel in ans:
            vowel_num += 1
    if vowel_num > 0 and len(ans) - vowel_num > 1:
        return True
    else:
        return False


def combination(length, letters):
    import itertools
    for ans in itertools.combinations(letters, length):
        if validation(ans):
            print(''.join(ans))


def recursion(length, letters, ans, index=0):
    if length == len(ans) and validation(ans):
        print(''.join(ans))
        return 0
    if len(letters) == index:
        return 0
    ans.append(letters[index])
    recursion(length, letters, ans, index+1)
    ans.pop()
    recursion(length, letters, ans, index+1)
    return 0


def main(mode=''):
    l, c = (int(x) for x in read().split())
    letters = read().split()
    letters.sort()
    if mode == 'permutation':
        combination(l, letters)
    else:
        ans = []
        recursion(l, letters, ans)


if __name__ == '__main__':
    main('permutation')
