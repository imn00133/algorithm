# 09 최단 경로 - 전보
# Solved Date: 22.07.10.
import sys
import heapq

read = sys.stdin.readline
INT = int(1e9)


def dijkstra(arr, start):
    cost_min_table = [INT for _ in range(len(arr))]
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, city = heapq.heappop(pq)
        if cost_min_table[city] < cost:
            continue

        for next_city, current_min_cost in arr[city]:
            new_cost = cost + current_min_cost
            if cost_min_table[next_city] < new_cost:
                continue
            cost_min_table[next_city] = new_cost
            heapq.heappush(pq, (new_cost, next_city))

    connection_city, max_cost = 0, 0
    for cost in cost_min_table:
        if cost == INT:
            continue
        connection_city += 1
        max_cost = max(max_cost, cost)
    return connection_city, max_cost


def main():
    city_num, path_num, city = (int(x) for x in read().split())
    arr = [[] for _ in range(city_num+1)]
    for _ in range(path_num):
        current_city, next_city, cost = (int(x) for x in read().split())
        arr[current_city].append((next_city, cost))
    print(*dijkstra(arr, city))


if __name__ == '__main__':
    main()
