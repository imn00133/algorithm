# 15 이진 탐색 - 고정점 찾기
# Solved Date: 22.05.14.
import sys
read = sys.stdin.readline


def find_anchor(arr):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if mid > arr[mid]:
            left = mid + 1
        elif mid < arr[mid]:
            right = mid
        else:
            return mid
    return -1


def main():
    arr_num = int(read())
    arr = [int(x) for x in read().split()]
    print(find_anchor(arr))


if __name__ == '__main__':
    main()
