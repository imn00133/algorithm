# 17 최단 경로 - 숨바꼭질
# Solved Date: 22.07.17.
import sys
import heapq

INF = int(1e9)
read = sys.stdin.readline


def answer(cost_table):
    answer_node, answer_dist, answer_count = 0, 0, 0
    for index, cost in enumerate(cost_table, 1):
        if cost > answer_dist:
            answer_node = index
            answer_dist = cost
            answer_count = 1
        elif cost == answer_dist:
            answer_count += 1
    return answer_node, answer_dist, answer_count


def dijkstra(arr):
    cost_table = [INF for _ in range(len(arr))]
    start_node = 0
    cost_table[start_node] = 0
    hq = []
    heapq.heappush(hq, (0, 0))

    while hq:
        current_cost, node = heapq.heappop(hq)
        if current_cost > cost_table[node]:
            continue
        for next_node in arr[node]:
            next_cost = current_cost + 1
            if next_cost > cost_table[next_node]:
                continue
            cost_table[next_node] = next_cost
            heapq.heappush(hq, (next_cost, next_node))

    return answer(cost_table)


def main():
    n, m = (int(x) for x in read().split())
    arr = [[] for _ in range(n)]
    for _ in range(m):
        start, end = (int(x) for x in read().split())
        arr[start-1].append(end-1)
        arr[end-1].append(start-1)
    print(*dijkstra(arr))


if __name__ == '__main__':
    main()
