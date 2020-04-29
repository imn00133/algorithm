# https://www.acmicpc.net/problem/14226
# Solved Date: 20.04.29.

import sys
import collections

read = sys.stdin.readline
MAX = 1000


def bfs(find_emoticon):
    emoticon_arr = [[-1 for _ in range(MAX + 1)] for _ in range(MAX + 1)]
    queue = collections.deque()
    # 현재 이모티콘/클립보드
    time = 0
    queue.append((1, 0, time))
    emoticon_arr[1][0] = time
    while queue:
        emoticon, clipboard, time = queue.popleft()
        time += 1
        # 1번
        if emoticon_arr[emoticon][emoticon] == -1:
            emoticon_arr[emoticon][emoticon] = time
            queue.append((emoticon, emoticon, time))
        # 2번
        next_emoticon = emoticon + clipboard
        if next_emoticon <= MAX and emoticon_arr[next_emoticon][clipboard] == -1 and clipboard:
            emoticon_arr[next_emoticon][clipboard] = time
            queue.append((next_emoticon, clipboard, time))
            # 가장 빠른 시간을 찾음으로, 같아지면 답을 찾은 것이다.
            if next_emoticon == find_emoticon:
                return time
        # 3번
        if emoticon > 1 and emoticon_arr[emoticon-1][clipboard] == -1:
            emoticon_arr[emoticon-1][clipboard] = time
            queue.append((emoticon-1, clipboard, time))
            if emoticon - 1 == find_emoticon:
                return time


def main():
    emoticon = int(read().strip())
    print(bfs(emoticon))


if __name__ == '__main__':
    main()
