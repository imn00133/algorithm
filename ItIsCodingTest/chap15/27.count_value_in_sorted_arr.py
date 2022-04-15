# 15 이진 탐색 - 정렬된 배열에서 특정 수의 개수 구하기
# Solved Date: 22.04.15.
import sys

read = sys.stdin.readline

# 값이 중간일 때가 처리가 안됨
# # x보다 작은 값을 구함
# def lower_binary_exploration(arr, x):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         mid = (left + right) // 2 + 1
#         if arr[mid] >= x:
#             right = mid - 1
#         else:
#             left = mid
#     return left
#
#
# # x보다 큰 값을 구함
# def upper_binary_exploration(arr, x):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid
#     return left


# x의 최소 인덱스를 구함
def lower_binary_exploration(arr, x):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


# x의 최대 인덱스를 구함
def upper_binary_exploration(arr, x):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2 + 1
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid
    return left


# 값이 최대값보다 클때, 값이 최소값보다 작을 때, 값이 중간일때
# upper - lower 최댓값, 최솟값 => 0, 값이 중간일 때 => -1
def main():
    n, x = (int(x) for x in read().split())
    arr = [int(x) for x in read().split()]
    lower = lower_binary_exploration(arr, x)
    upper = upper_binary_exploration(arr, x)
    if upper - lower <= 0:
        return -1
    return upper - lower + 1


if __name__ == '__main__':
    print(main())
