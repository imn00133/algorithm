# https://www.acmicpc.net/problem/5427
# Solved Date: 20.04.27.

import sys
import collections

DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))
read = sys.stdin.readline


def find(building, mark):
    # 이 함수를 둘 다 찾게 만들어도 10ms차이밖에 안 난다.
    pos = []
    for y in range(len(building)):
        for x in range(len(building[0])):
            if building[y][x] == mark:
                pos.append((y, x))
    return pos


def bfs(building):
    column, row = len(building), len(building[0])
    # pos는 y, x로 구성
    fire_queue = collections.deque(find(building, '*'))
    man_queue = collections.deque(find(building, '@'))
    # 시작 때, 맞으면 바로 탈출한다.
    if man_queue[0][0] == 0 or man_queue[0][0] == column - 1 or \
            man_queue[0][1] == 0 or man_queue[0][1] == row - 1:
        return 1
    count = 0
    while True:
        # temp에 저장하게 만들어, queue의 첫 값을 지속적으로 확인하지 않으면 100ms가 빨라짐
        # 처음에는 queue내에 second도 저장했었음
        # 40KB를 더 소모함
        temp_fire_queue = collections.deque()
        while fire_queue:
            y, x = fire_queue.popleft()
            for dy, dx in DYX:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < column and 0 <= new_x < row and \
                        (building[new_y][new_x] == '.' or building[new_y][new_x] == '@'):
                    building[new_y][new_x] = '*'
                    temp_fire_queue.append((new_y, new_x))

        temp_man_queue = collections.deque()
        while man_queue:
            y, x = man_queue.popleft()
            for dy, dx in DYX:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < column and 0 <= new_x < row and building[new_y][new_x] == '.':
                    building[new_y][new_x] = '@'
                    temp_man_queue.append((new_y, new_x))
                    if new_y == 0 or new_y == column - 1 or new_x == 0 or new_x == row - 1:
                        # 끝에 도착하였으나, count가 변경되지 않음 + 마지막에 밖으로 나가는 시간 추가
                        count += 2
                        return count

        fire_queue = temp_fire_queue
        man_queue = temp_man_queue
        count += 1
        if not man_queue:
            return "IMPOSSIBLE"


def main():
    test_case = int(read().strip())
    for _ in range(test_case):
        width, height = (int(x) for x in read().split())
        building = []
        for _ in range(height):
            building.append(list(read().strip()))
        print(bfs(building))


if __name__ == '__main__':
    main()
