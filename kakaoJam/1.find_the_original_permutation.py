# https://www.hackerrank.com/contests/kakao-adtech-devday-1st-codejam/challenges/find-the-original-permutation
# Solved Date: 22.04.14.

import sys

read = sys.stdin.readline


def simple_answer(arr, arr_num):
    answer = ["" for _ in range(arr_num)]

    for value, position in enumerate(arr, 1):
        save_position = position
        index = 0
        while save_position >= index:
            if not answer[index]:
                index += 1
                continue
            save_position += 1
            index += 1
        answer[save_position] = str(value)
    return " ".join(answer)


# fail
def fast_answer(arr, arr_num):
    answer = ["" for _ in range(arr_num)]

    for index in range(len(arr)):
        number = index + 1
        save_position = arr[index]
        for sub_index in range(index):
            if arr[sub_index] <= save_position:
                save_position += 1
        # 9, 10 반대는 처리하지 못함.
        while answer[save_position]:
            save_position += 1
        answer[save_position] = str(number)
        arr[index] = save_position
    return " ".join(answer)


if __name__ == '__main__':
    arr_num = int(read().rstrip())
    arr = [int(x) for x in read().split()]

    print(fast_answer(arr, arr_num))
