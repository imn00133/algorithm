# https://www.acmicpc.net/problem/17619
# Solved Date:

import sys
import collections

read = sys.stdin.readline


class Node:
    def __init__(self, index, start, end, prev_node=None):
        self.index = index
        self.start = start
        self.end = end
        self.prev_node = prev_node
        self.next_node = None


def add_graph(graph, index, con_index):
    if index not in graph[con_index]:
        graph[index].append(con_index)
        graph[con_index].append(index)


def change_end(node, graph):
    while node.next_node is not None:
        next_s, next_e, next_index = node.next_node.start, node.next_node.end, node.next_node.index
        if node.end < next_s:
            # end < ns < ne
            break
        elif node.end < next_e:
            # ns <= end < ne
            add_graph(graph, node.index, next_index)
            node.end = next_e
            # 다음 node를 다 다음 node로 변경
            node.next_node = node.next_node.next_node
            if node.next_node is not None:
                node.next_node.prev_node = node
            break
        else:
            # ne < end, 즉 완전히 종속됨
            add_graph(graph, node.index, next_index)
            node.next_node = node.next_node.next_node
            if node.next_node is not None:
                node.next_node.prev_node = node


def change_start(node, graph):
    while node.prev_node is not None:
        prev_s, prev_e, prev_index = node.prev_node.start, node.prev_node.end, node.prev_node.index
        if prev_e > node.start:
            # pe > start
            break
        elif prev_s > node.start:
            # ps > start >= pe
            add_graph(graph, node.index, prev_index)
            node.index = prev_index
            node.start = prev_s
            # 이전 노드를 이이전 노드로 변경
            node.prev_node = node.prev_node.prev_node
            if node.prev_node is not None:
                node.prev_node.next_node = node
            break
        else:
            # start > ps, 즉 완전히 종속됨
            add_graph(graph, node.index, prev_index)
            node.index = prev_index
            node.prev_node = node.prev_node.prev_node
            if node.prev_node is not None:
                node.prev_node.next_node = node


def greedy_read(log_num):
    graph = [[] for _ in range(log_num+1)]
    first = [int(x) for (x) in read().split()]
    node_head = Node(1, first[0], first[1])
    for index in range(2, log_num+1):
        log = [int(x) for(x) in read().split()]
        log_s, log_e = log[0], log[1]
        node = node_head
        while True:
            if log_s < node.start:
                if log_e < node.start:
                    # ls < le < s
                    new_node = Node(index, log_s, log_e, node.prev_node)
                    new_node.next_node = node
                    node.prev_node = new_node
                    break
                elif node.start <= log_e <= node.end:
                    # ls < s <= le <= e
                    add_graph(graph, node.index, index)
                    node.index = index
                    node.start = log_s
                    change_start(node, graph)
                    break
                elif node.end < log_e:
                    # ls < s < e < le
                    add_graph(graph, node.index, index)
                    node.index = index
                    node.start = log_s
                    node.end = log_e
                    change_start(node, graph)
                    change_end(node, graph)
                    break
            elif node.start <= log_s <= node.end:
                if log_e <= node.end:
                    # s <= ls < le <= e
                    add_graph(graph, node.index, index)
                    break
                elif node.end < log_e:
                    # s <= ls <= e < le
                    add_graph(graph, node.index, index)
                    node.end = log_e
                    change_end(node, graph)
            # e < ls < le
            if node.next_node is None:
                node.next_node = Node(index, log_s, log_e, node)
                break
            else:
                node = node.next_node
    return graph


def find_ans(graph, start, end):
    check = [False for _ in range(len(graph))]
    queue = collections.deque()
    check[start] = True
    queue.append(start)
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if check[next_node]:
                continue
            if next_node == end:
                return 1
            check[next_node] = True
            queue.append(next_node)
    return 0


def slow_linked_list():
    log_num, question_num = (int(x) for x in read().split())
    graph = greedy_read(log_num)
    for _ in range(question_num):
        start, end = (int(x) for x in read().split())
        print(find_ans(graph, start, end))


if __name__ == '__main__':
    slow_linked_list()
