# 14 정렬 - 안테나
# Solved Date: 22.04.15.
# https://www.acmicpc.net/problem/18310
import sys

read = sys.stdin.readline


# Counter를 빼니 180 -> 160이 됨
# 서버가 불안정한지 왔다갔다하긴 하지만, 대충 20ms차이가 남
def fast_solve():
    house_pos = [int(x) for x in read().split()]
    house_pos.sort()
    return house_pos[(len(house_pos) - 1) // 2]


# 현재 기준점을 움직이면서 계산
# 맨 오른쪽 값을 잡았을 때 왼쪽 length를 계산하고, 이를 초기로 둠
# current pos를 두면, 오른쪽 길이는 (prev_pos - current_pos) * right house count가 됨
# 왼쪽 길이는 기준점이 줄어든 것이기 때문에 (prev_pos - current_pos) * left house count만큼 줄어듬
# 이를 반복해서 최소를 구함
def solve():
    from collections import Counter
    house_pos_count = Counter((int(x) for x in read().split()))
    pos_sort = sorted(house_pos_count.keys())
    prev_pos = pos_sort.pop()

    min_len = 0
    left_house_count = 0
    right_house_count = house_pos_count[prev_pos]
    for pos, house_count in house_pos_count.items():
        if pos == prev_pos:
            continue
        left_house_count += house_count
        min_len += (prev_pos - pos) * house_count

    answer = prev_pos
    left_len = min_len
    right_len = 0
    for index in range(1, len(pos_sort)+1):
        current_pos = pos_sort[-index]
        current_count = house_pos_count[current_pos]
        current_diff = prev_pos - current_pos
        right_len += current_diff * right_house_count
        right_house_count += current_count

        left_len -= current_diff * left_house_count
        left_house_count -= current_count

        current_len = left_len + right_len
        if min_len < current_len:
            continue

        min_len = current_len
        answer = current_pos
    return answer


def main():
    whole_house = int(read().rstrip())

    print(fast_solve())


if __name__ == '__main__':
    main()
