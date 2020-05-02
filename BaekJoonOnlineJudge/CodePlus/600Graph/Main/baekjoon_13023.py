# https://www.acmicpc.net/problem/13023
# Solved Date: 20.04.20.

import sys
read = sys.stdin.readline


def dfs(relations, check, person=0, deep_index=0, flag=False):
    check[person] = True
    if deep_index == 4 or flag:
        flag = True
        return flag
    for next_person in relations[person]:
        if not check[next_person]:
            flag = dfs(relations, check, next_person, deep_index+1, flag)
        if flag:
            break
    check[person] = False
    return flag


def dfs_all(people_num, relations):
    check = [False for _ in range(people_num)]
    for person in range(people_num):
        if dfs(relations, check, person):
            return True
    return False


def main():
    people_num, relation_num = (int(x) for x in read().split())
    relations = [[] for _ in range(people_num)]
    for _ in range(relation_num):
        rel = [int(x) for x in read().split()]
        relations[rel[0]].append(rel[1])
        relations[rel[1]].append(rel[0])
    if dfs_all(people_num, relations):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
