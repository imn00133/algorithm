# 07 이진 탐색 - 부품 찾기
# Solved Date: 22.04.15.
import sys

read = sys.stdin.readline


def calc_guest_rice_cake_length(arr, cutting):
    total = 0
    for rice_cake in arr:
        if rice_cake <= cutting:
            continue
        total += rice_cake - cutting
    return total


# 맨날 헷갈리는 right = mid - 1, left = mid
def binary_exploration(arr, ask_length):
    left = 0
    right = 10 ** 9
    while left < right:
        mid = (left + right) // 2 + 1

        if calc_guest_rice_cake_length(arr, mid) < ask_length:
            right = mid - 1
            continue
        left = mid
    return left


def main():
    num, ask_length = (int(x) for x in read().split())
    arr = [int(x) for x in read().split()]
    print(binary_exploration(arr, ask_length))


if __name__ == '__main__':
    main()
