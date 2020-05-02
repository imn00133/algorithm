# https://www.acmicpc.net/problem/13549
# Solved Date: 20.04.29.

import sys
import collections
read = sys.stdin.readline

MAX = 100000


def check_node(next_node):
    if 0 <= next_node <= MAX:
        return True
    else:
        return False


def bfs(start, end):
    # start에서 돌아가는 방법
    time = [-1 for _ in range(MAX + 1)]
    deck = collections.deque()
    time[start] = 0
    deck.append(start)
    while deck:
        node = deck.popleft()
        second = time[node]
        if node == end:
            return second
        next_node = 2 * node
        if check_node(next_node) and time[next_node] == -1:
            time[next_node] = second
            deck.appendleft(next_node)
        for next_node in [node + 1, node - 1]:
            if check_node(next_node) and time[next_node] == -1:
                time[next_node] = second + 1
                deck.append(next_node)


def reverse_bfs(start, end):
    # end에서 돌아가는 방법
    # https://www.acmicpc.net/source/12222800 참고
    time = [MAX for _ in range(MAX + 1)]
    deck = collections.deque()
    time[end] = 0
    deck.append(end)
    while deck:
        node = deck.popleft()
        second = time[node]
        if node == start:
            return second
        if not (node % 2) and time[node // 2] > second:
            next_node = node // 2
            time[next_node] = second
            deck.appendleft(next_node)
        if 0 <= node - 1 and time[node - 1] > second:
            next_node = node - 1
            time[next_node] = second + 1
            deck.append(next_node)
        if node + 1 <= MAX and time[node + 1] > second:
            next_node = node + 1
            time[next_node] = second + 1
            deck.append(next_node)


def main():
    start, end = (int(x) for x in read().split())
    if start < end:
        print(bfs(start, end))
    else:
        print(start - end)


if __name__ == '__main__':
    main()
