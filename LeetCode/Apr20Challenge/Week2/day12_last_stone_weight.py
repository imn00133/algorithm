# https://leetcode.com/problems/last-stone-weight/
# Solved Date: 20.04.13.
# heapq의 사용은 diary를 참고한다.


def heapq_use_last_stone_weight(stones):
    import heapq
    h = [-x for x in stones]
    heapq.heapify(h)
    while len(h) > 1 and h[0] != 0:
        diff = heapq.heappop(h) - heapq.heappop(h)
        heapq.heappush(h, diff)
    return -h[0]


def last_stone_weight(stones):
    while True:
        stones.sort()
        if len(stones) == 1 or len(stones) == 0:
            break
        x, y = stones.pop(), stones.pop()
        if x != y:
            stones.append(x-y)
    if len(stones) == 1:
        return stones[0]
    else:
        return 0


def main():
    stones = [int(x) for x in input().split()]
    print(last_stone_weight(stones))


if __name__ == '__main__':
    main()
