# https://www.acmicpc.net/problem/2343
# Solved Date: 20.05.17.

import sys
read = sys.stdin.readline


def blue_ray_count(lesson_lengths, blue_ray_length):
    count = 1
    recorded_length = 0
    for length in lesson_lengths:
        if recorded_length + length > blue_ray_length:
            count += 1
            recorded_length = length
        else:
            recorded_length += length
    return count


def binary_search(lesson_lengths, expected_count):
    left = max(lesson_lengths)
    # https://www.acmicpc.net/source/19245920 최대값 참고
    right = sum(lesson_lengths)
    while left < right:
        mid = (left + right) // 2
        if blue_ray_count(lesson_lengths, mid) > expected_count:
            left = mid + 1
        else:
            right = mid
    return left


def main():
    lesson_num, expected_count = (int(x) for x in read().split())
    lesson_lengths = [int(x) for x in read().split()]
    print(binary_search(lesson_lengths, expected_count))


if __name__ == '__main__':
    main()
