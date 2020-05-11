# https://leetcode.com/problems/find-the-town-judge
# Solved Date: 20.05.10.

import collections


class Solution:
    def find_judge(self, N: int, trust: list[list[int]]) -> int:
        trust_dict = {}
        for person in range(1, N+1):
            trust_dict[person] = []
        for person, trusted in trust:
            if not trust_dict:
                break
            if person in trust_dict:
                trust_dict.pop(person)
            if trusted in trust_dict:
                trust_dict[trusted].append(person)
        if len(trust_dict) == 1:
            for value in trust_dict.values():
                if len(value) == N-1:
                    return list(trust_dict.keys())[0]
        return -1

    def fast_find_judge(self, N: int, trust: list[list[int]]) -> int:
        trust_counter = [0 for _ in range(N+1)]
        for person, trusted in trust:
            trust_counter[person] -= 1
            trust_counter[trusted] += 1
        for person in range(1, len(trust_counter)):
            if trust_counter[person] == N - 1:
                return person
        return -1
