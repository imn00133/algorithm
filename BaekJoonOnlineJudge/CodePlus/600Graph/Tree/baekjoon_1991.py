# https://www.acmicpc.net/problem/1991
# Solved Date: 20.04.30.

import sys
read = sys.stdin.readline

MAX = 26
NONE = ord('.') - ord('A')


def pre_order(adj, node=0):
    if node == NONE:
        return 0
    print(chr(ord('A') + node), end='')
    pre_order(adj, adj[node][0])
    pre_order(adj, adj[node][1])


def in_order(adj, node=0):
    if node == NONE:
        return 0
    in_order(adj, adj[node][0])
    print(chr(ord('A') + node), end='')
    in_order(adj, adj[node][1])


def post_order(adj, node=0):
    if node == NONE:
        return 0
    post_order(adj, adj[node][0])
    post_order(adj, adj[node][1])
    print(chr(ord('A') + node), end='')


def main():
    adjacency_list = [[] for _ in range(MAX)]
    arr_num = int(read().strip())
    for _ in range(arr_num):
        temp = [ord(x) - ord('A') for x in read().split()]
        adjacency_list[temp[0]].extend(temp[1:])
    pre_order(adjacency_list)
    print()
    in_order(adjacency_list)
    print()
    post_order(adjacency_list)


if __name__ == '__main__':
    main()
