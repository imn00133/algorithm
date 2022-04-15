# 07 이진 탐색 - 부품 찾기
# Solved Date: 22.04.15.
import sys

read = sys.stdin.readline


def solve_list(office_parts, guest_ask_parts):
    parts_arr = [False for _ in range(10**6+1)]
    for part in office_parts:
        parts_arr[part] = True

    answer = []
    for ask_part in guest_ask_parts:
        is_in_parts = "no"
        if parts_arr[ask_part]:
            is_in_parts = "yes"
        answer.append(is_in_parts)
    return " ".join(answer)


def solve_set(office_parts, guest_ask_parts):
    parts = set(office_parts)
    answer = []
    for ask_part in guest_ask_parts:
        is_in_parts = "no"
        if ask_part in parts:
            is_in_parts = "yes"
        answer.append(is_in_parts)
    return " ".join(answer)


def main():
    n = int(read().rstrip())
    office_parts = [int(x) for x in read().split()]
    m = int(read().rstrip())
    guest_ask_parts = [int(x) for x in read().split()]
    print(solve_list(office_parts, guest_ask_parts))


if __name__ == '__main__':
    main()
