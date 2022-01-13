# chap11 그리디 - 무지의 먹방 라이브
# Solved Date: 22.01.13.
# https://programmers.co.kr/learn/courses/30/lessons/42891

import sys
import collections

read = sys.stdin.readline


def find_final_food_index(food_times_index, k):
    prev_food_time = 0
    prev_food_index = 0
    for index, (food_time, food_index) in enumerate(food_times_index):
        if food_time == prev_food_time:
            continue

        current_food_time = food_time - prev_food_time
        remainder_len = len(food_times_index) - index
        next_k = k - (current_food_time * remainder_len)

        if next_k >= 0:
            prev_food_time = food_time
            prev_food_index = food_index
            k = next_k
            continue

        return prev_food_time, prev_food_index, ((k + 1) % remainder_len)

    return -1, -1, -1


def find_answer_index(food_times, base_food_time, base_food_index, remainder):
    for index in range(len(food_times)):
        check_index = (index + base_food_index) % len(food_times)
        if remainder == 0:
            return check_index
        if food_times[check_index] >= base_food_time:
            remainder -= 1


def fail_solution(food_times, k):
    food_times_index = [(food_time, index) for index, food_time in enumerate(food_times)]
    food_times_index.sort()

    base_food_time, base_food_index, remainder = find_final_food_index(food_times_index, k)
    if base_food_time < 0:
        return -1

    return find_answer_index(food_times, base_food_time, base_food_index, remainder) + 1


def find_remainder_k(food_times_len, food_time_counter, k):
    sort_food_time = sorted(food_time_counter.keys())
    prev_food_time = 0
    cal_complete_len = 0
    for food_index, food_time in enumerate(sort_food_time):
        current_food_time = food_time - prev_food_time
        current_len = food_times_len - cal_complete_len
        next_k = k - (current_food_time * current_len)

        if next_k > 0:
            k = next_k
            prev_food_time = food_time
            cal_complete_len += food_time_counter[food_time]
            continue

        # 0이면서 다음 index가 있을 수는 없음(전체 크기 > k)
        # -1로 찾으면 바로 반환하도록 함
        if next_k == 0:
            k = next_k
            return sort_food_time[food_index + 1], k - 1

        # k+1을 할 경우, index문제가 있음 -> k로 하고, 계산 때 1번 더 돌도록 함
        if next_k < 0:
            return food_time, k % current_len


def solution(food_times, k):
    food_time_counter = collections.defaultdict(int)
    sum_food_time = 0
    for food_time in food_times:
        sum_food_time += food_time
        food_time_counter[food_time] += 1

    if sum_food_time <= k:
        return -1

    answer_food_time, remainder_k = find_remainder_k(len(food_times), food_time_counter, k)

    for index, food_time in enumerate(food_times):
        if food_time >= answer_food_time:
            remainder_k -= 1
            if remainder_k >= 0:
                continue
            return index + 1


if __name__ == '__main__':
    k = int(read().rstrip())
    food_times = [int(x) for x in read().split()]
    print(solution(food_times, k))
