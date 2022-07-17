# 10 그래프 이론 - 커리큘럼
# Solved Date: 22.07.17.
import sys
from collections import deque
import heapq

read = sys.stdin.readline


# 위상정렬하고, 더 오래 걸리는 값을 항상 저장해줌
def book_topological_sort(indegrees, graph, costs):
    answer = [cost for cost in costs]
    queue = deque()
    for node, indegree in enumerate(indegrees):
        if indegree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            answer[next_node] = max(answer[next_node], answer[node] + costs[next_node])
            indegrees[next_node] -= 1
            if indegrees[next_node] ==  0:
                queue.append(next_node)

    return "\n".join([str(x) for x in answer])


# heapq를 통해 정렬하면 항상 최소로 강의 종료시간이 나온다는 점을 이용
def topological_sort(indegrees, graph, costs):
    hq = []
    for node, indegree in enumerate(indegrees):
        if indegree == 0:
            heapq.heappush(hq, (costs[node], node))

    answer = ["" for _ in range(len(indegrees))]
    while hq:
        current_cost, node = heapq.heappop(hq)
        answer[node] = str(current_cost)
        for next_node in graph[node]:
            indegrees[next_node] -= 1
            if indegrees[next_node] == 0:
                heapq.heappush(hq, (current_cost + costs[next_node], next_node))
    return "\n".join(answer)


def main():
    n = int(read().rstrip())
    indegrees = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    costs = [0 for _ in range(n)]
    for node in range(n):
        for value_index, value in enumerate((int(x) for x in read().split())):
            if value_index == 0:
                costs[node] = value
                continue

            if value == -1:
                break

            indegrees[node] += 1
            graph[value-1].append(node)
    return print(book_topological_sort(indegrees, graph, costs))


if __name__ == '__main__':
    main()
