# 10 그래프 이론 - 도시 분할 계획
# Solved Date: 22.07.17.
# https://www.acmicpc.net/problem/1647
import sys
import heapq

read = sys.stdin.readline


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union(parents, pos):
    a, b = pos
    parent_a = find_parent(parents, a)
    parent_b = find_parent(parents, b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b


def is_cycle(parents, pos):
    a, b = pos
    return find_parent(parents, a) == find_parent(parents, b)


def heap_kruskal(hq, n):
    parents = [i for i in range(n)]
    total_cost = 0
    end_cost = 0
    while hq:
        cost, pos = heapq.heappop(hq)
        if is_cycle(parents, pos):
            continue
        total_cost += cost
        end_cost = cost
        union(parents, pos)
    return total_cost - end_cost


# 6788ms
def heap_answer(n, m):
    hq = []
    for _ in range(m):
        a, b, cost = (int(x) for x in read().split())
        heapq.heappush(hq, (cost, (a-1, b-1)))
    return heap_kruskal(hq, n)


def sort_kruskal(edge, n):
    parents = [i for i in range(n)]
    total_cost = 0
    end_cost = 0
    while edge:
        cost, pos = edge.pop()
    # pop을 쓰면 느린가..?(3460ms) -> pop이 더 빠름(3716ms)
    # for cost, pos in edge:
        if is_cycle(parents, pos):
            continue
        total_cost += cost
        end_cost = cost
        union(parents, pos)
    return total_cost - end_cost


# 참고: https://www.acmicpc.net/source/33569310
# 3460ms
def sort_answer(n, m):
    edge = []
    for _ in range(m):
        a, b, cost = (int(x) for x in read().split())
        edge.append((cost, (a-1, b-1)))
    edge.sort(key=lambda x: x[0], reverse=True)
    return sort_kruskal(edge, n)


def main():
    n, m = (int(x) for x in read().split())
    print(sort_answer(n, m))


if __name__ == '__main__':
    main()
