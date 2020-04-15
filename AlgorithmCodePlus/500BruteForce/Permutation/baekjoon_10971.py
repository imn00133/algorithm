# https://www.acmicpc.net/problem/10971
# Solved Date: 20.04.15.

import sys
read = sys.stdin.readline

MAX_COST = 1000000


def brute_force(nums, costs):
    import itertools
    cost_min = MAX_COST * 10 + 1
    for way in itertools.permutations(nums):
        way_cost = 0
        if way[0] != 0:
            break
        for index in range(len(way)-1):
            cost = costs[way[index]][way[index+1]]
            if cost == 0:
                way_cost = 0
                break
            else:
                way_cost += cost
        # 0일 경우 갈 수 없기 때문에, 둘 다 값이 있어야 성립한다.
        if not (way_cost and costs[way[-1]][way[0]]):
            continue
        way_cost += costs[way[-1]][way[0]]
        cost_min = min(cost_min, way_cost)
    return cost_min


def main():
    arr_num = int(read().strip())
    nums = [x for x in range(arr_num)]
    costs = []
    for _ in range(arr_num):
        costs.append([int(x) for x in read().split()])
    print(brute_force(nums, costs))


if __name__ == '__main__':
    main()
