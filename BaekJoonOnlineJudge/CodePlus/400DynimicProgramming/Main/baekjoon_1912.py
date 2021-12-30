# https://www.acmicpc.net/problem/1912
# Solved Date: 20.04.02.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

dp_arr = []


def bottom_up(sequence):
    dp_arr.append(sequence[0])
    for index, value in enumerate(sequence[1:], 1):
        if dp_arr[index-1] > 0:
            dp_arr.append(dp_arr[index-1] + value)
        else:
            dp_arr.append(value)


def top_down(sequence, end):
    if end == 0:
        dp_arr.append(sequence[0])
        return dp_arr[0]
    if end == len(dp_arr) - 1:
        return dp_arr[-1]
    if len(sequence) > len(dp_arr) + 1:
        top_down(sequence, end-1)
    if dp_arr[-1] > 0:
        dp_arr.append(dp_arr[-1] + sequence[end])
    else:
        dp_arr.append(sequence[end])


def main(mode=''):
    arr_num = int(read().strip())
    sequence = [int(x) for x in read().split()]
    if mode == 'top':
        if arr_num > 1000:
            for i in range(1000, arr_num, 1000):
                top_down(sequence, i-1)
        top_down(sequence, arr_num-1)
    else:
        bottom_up(sequence)
    print(max(dp_arr))


def make_sequence(num):
    import random
    sequence = []
    for _ in range(num):
        sequence.append(random.randint(-1000, 1000))
    return sequence


def init_dp_arr():
    for _ in range(len(dp_arr)):
        dp_arr.pop()


def test():
    while True:
        num = int(input("sequence 값: "))
        if num <= 0:
            break

        init_dp_arr()
        sequence = make_sequence(num)
        bottom_up(sequence)
        bottom_max = max(dp_arr)
        bottom_dp = dp_arr[:]

        init_dp_arr()
        if num > 1000:
            for i in range(1000, num, 1000):
                top_down(sequence, i)
        top_down(sequence, num-1)
        top_max = max(dp_arr)

        if bottom_max != top_max:
            print("top_down 오류")
            print("bottom_max:", bottom_max)
            print("top_max:", top_max)
            print("bottom_dp:", bottom_dp)
            print("top_dp:   ", dp_arr)
            print("sequence:", sequence)
            for index, value in enumerate(bottom_dp):
                if dp_arr[index] != value:
                    print(index)
                    print(dp_arr[index], value)
                    print(sequence[index])
                    break
            print()
        else:
            print("성공")
            print()


if __name__ == '__main__':
    main('top')
