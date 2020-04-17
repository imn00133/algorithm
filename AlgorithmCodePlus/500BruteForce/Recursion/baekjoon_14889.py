# https://www.acmicpc.net/problem/14889
# Solved Date: 20.04.17.

import sys
import itertools
read = sys.stdin.readline


def stats_calc(stats, ans):
    a_stat = 0
    for i, j in itertools.permutations(ans, 2):
        a_stat += stats[i][j]

    b_people = []
    for x in range(len(stats)):
        if x not in ans:
            b_people.append(x)

    b_stat = 0
    for i, j in itertools.permutations(b_people, 2):
        b_stat += stats[i][j]
    return abs(a_stat - b_stat)


def recursion(n, stats, ans, index=0):
    if n == 0:
        return stats_calc(stats, ans)
    elif len(stats) == index:
        # 나올 수 있는 대략적인 최대값
        return 10000
    ans.append(index)
    select_diff_score = recursion(n-1, stats, ans, index+1)
    ans.pop()
    min_diff_score = min(select_diff_score, recursion(n, stats, ans, index+1))
    return min_diff_score


def combination(stats):
    people = list(range(len(stats)))
    min_diff_score = 10000
    for team in itertools.combinations(people, len(stats)//2):
        min_diff_score = min(min_diff_score, stats_calc(stats, team))
    return min_diff_score


def main(mode=''):
    arr_num = int(read().strip())
    stats = []
    for _ in range(arr_num):
        stats.append([int(x) for x in read().split()])
    if mode == 'recursion':
        ans = []
        print(recursion(arr_num//2, stats, ans))
    else:
        print(combination(stats))


if __name__ == '__main__':
    main()
