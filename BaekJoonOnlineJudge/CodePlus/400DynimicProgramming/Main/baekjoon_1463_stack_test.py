# https://www.acmicpc.net/problem/1463
# Solved Date: 20.03.30.
# 전역변수는 보통 사용하지 않는게 좋다고 알지만, 알고리즘 풀이에서는 어느정도 사용해도 좋다.
# 재귀 제한을 풀어도 stack size를 넘기 때문에, num을 나눠서 구현하였다.
# 자세한 사항은 diary를 참고할 것

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**4)

MAX_NUM = 1000000
dp_arr = [0 for _ in range(MAX_NUM + 1)]


def bottom_up(num):
    for i in range(2, num+1):
        dp_arr[i] = dp_arr[i-1] + 1
        if i % 2 == 0:
            dp_arr[i] = min(dp_arr[i], dp_arr[i//2] + 1)
        if i % 3 == 0:
            dp_arr[i] = min(dp_arr[i], dp_arr[i//3] + 1)
    return dp_arr[num]


def top_down(num):
    if num % 1000 == 0:
        print(num)
    if num == 1:
        return 0
    if dp_arr[num] > 0:
        return dp_arr[num]
    dp_arr[num] = top_down(num-1) + 1
    if num % 2 == 0:
        temp = top_down(num//2) + 1
        if temp < dp_arr[num]:
            dp_arr[num] = temp
    if num % 3 == 0:
        temp = top_down(num//3) + 1
        if temp < dp_arr[num]:
            dp_arr[num] = temp
    return dp_arr[num]


def main(mode='top'):
    num = int(read().strip())
    if mode == 'top' and num >= 1000:
        for part_num in range(1000, num+1, 1000):
            top_down(part_num)
        print(top_down(num))
    else:
        print(bottom_up(num))


def stack_test():
    # 20.04.02. diary참고
    sys.setrecursionlimit(10 ** 6)
    import threading
    threading.stack_size(200*1024*1024)
    thread = threading.Thread(target=top_down, args=(MAX_NUM,))
    thread.start()
    thread.join()
    print(dp_arr[100000])


def normal_test():
    sys.setrecursionlimit(10 ** 6)
    top_down(MAX_NUM)
    print(dp_arr[MAX_NUM])


if __name__ == '__main__':
    normal_test()
    main()
