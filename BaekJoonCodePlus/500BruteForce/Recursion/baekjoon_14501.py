# https://www.acmicpc.net/problem/14501
# Solved Date: 20.04.16.

import sys
read = sys.stdin.readline


def bottom_up(schedule):
    dp_arr = [0 for _ in range(len(schedule)+1)]
    for index in range(len(schedule)):
        if index + schedule[index][0] > len(schedule):
            continue
        if index != 0:
            dp_arr[index] = max(dp_arr[index], dp_arr[index-1])
        next_index = index + schedule[index][0]
        dp_arr[next_index] = max(dp_arr[next_index], dp_arr[index] + schedule[index][1])
    return max(dp_arr)


def recursion(schedule, salary=0, day=0):
    if day >= len(schedule):
        return salary
    if day + schedule[day][0] > len(schedule):
        select_salary = 0
    else:
        select_salary = salary + schedule[day][1]
    salary = max(salary, recursion(schedule, select_salary, day+schedule[day][0]),
                 recursion(schedule, salary, day+1))
    return salary


def main(mode=''):
    arr_num = int(read().strip())
    schedule = []
    for _ in range(arr_num):
        schedule.append([int(x) for x in read().split()])
    if mode == 'brute':
        print(recursion(schedule))
    else:
        print(bottom_up(schedule))


if __name__ == '__main__':
    main()
