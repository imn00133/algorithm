# https://www.acmicpc.net/problem/10808

import sys
read = sys.stdin.readline


def main():
    count_alphabet = [0 for _ in range(ord('z')-ord('a')+1)]
    string = read().strip()
    for letter in string:
        count_alphabet[ord(letter)-ord('a')] += 1
    for count in count_alphabet:
        print(count, end=" ")


if __name__ == '__main__':
    main()
