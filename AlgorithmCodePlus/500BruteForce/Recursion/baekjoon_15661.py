# https://www.acmicpc.net/problem/15661
# Solved Date: 20.04.17.

import sys
import itertools
read = sys.stdin.readline


def stats_calc(stats, ans):
    a_stat = 0
    if len(ans) >= 2:
        for i, j in itertools.permutations(ans, 2):
            a_stat += stats[i][j]

    b_people = []
    for x in range(len(stats)):
        if x not in ans:
            b_people.append(x)

    b_stat = 0
    if len(b_people) >= 2:
        for i, j in itertools.permutations(b_people, 2):
            b_stat += stats[i][j]
    return abs(a_stat - b_stat)


def recursion(n, stats, ans, index=0):
    if n == 0:
        return stats_calc(stats, ans)
    elif len(stats) == index:
        # 나올 수 있는 대략적인 최대값
        return 20000
    ans.append(index)
    select_diff_score = recursion(n-1, stats, ans, index+1)
    ans.pop()
    min_diff_score = min(select_diff_score, recursion(n, stats, ans, index+1))
    return min_diff_score


def combination(stats, n):
    people = list(range(len(stats)))
    min_diff_score = 10000
    for team in itertools.combinations(people, n):
        min_diff_score = min(min_diff_score, stats_calc(stats, team))
    return min_diff_score


def loop_arr(stats, mode):
    # python3로 시간초과
    # pypy3로 6.5s정도 걸림
    stat = []
    for n in range(1, len(stats) - 1):
        if mode == 'recursion':
            ans = []
            stat.append(recursion(n, stats, ans))
        else:
            stat.append(combination(stats, n))
    return min(stat)


def fast_calc(stats, team):
    stat = 0
    for i, j in itertools.permutations(team, 2):
        stat += stats[i][j]
    return stat


def fast_recursion(stats, t1, t2, index=0):
    # python3에서 시간초과
    # pypy3로 5.7s정도 걸림
    if index == len(stats):
        t1_stat = t2_stat = 0
        if len(t1) > 1:
            t1_stat = fast_calc(stats, t1)
        if len(t2) > 1:
            t2_stat = fast_calc(stats, t2)
        return abs(t1_stat - t2_stat)
    t1.append(index)
    diff_stat = fast_recursion(stats, t1, t2, index+1)
    t1.pop()
    t2.append(index)
    diff_stat = min(diff_stat, fast_recursion(stats, t1, t2, index+1))
    t2.pop()
    return diff_stat


def fast_loop(stats):
    # python3에서 시간초과
    # pypy3에서 3.9s
    # 절반이상 진행되면, 어쩌피 t1, t2가 반복임으로, 이를 제외하여 계산을 줄인다.
    diff_stat_min = 20000
    member = list(range(len(stats)))
    for n in range(1, len(stats)//2 + 1):
        for select_num in itertools.combinations(range(len(stats)), n):
            t1 = select_num
            t2 = []
            for index in member:
                if index not in t1:
                    t2.append(index)
            diff_stat_min = min(diff_stat_min, abs(fast_calc(stats, t1) - fast_calc(stats, t2)))
    return diff_stat_min


def main(select='', mode=''):
    arr_num = int(read().strip())
    stats = []
    for _ in range(arr_num):
        stats.append([int(x) for x in read().split()])
    if select == 'slow':
        print(loop_arr(stats, mode))
    elif select == 'fast_recursion':
        t1 = []
        t2 = []
        print(fast_recursion(stats, t1, t2))
    else:
        print(fast_loop(stats))


if __name__ == '__main__':
    main()
