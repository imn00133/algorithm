# https://www.acmicpc.net/problem/11664
# Solved Date: 20.05.16.

import sys
read = sys.stdin.readline

DIMENSION = 3


def distance(pos1, pos2):
    dist = 0
    for location1, location2 in zip(pos1, pos2):
        dist += (location1 - location2) ** 2
    return dist ** 0.5


def pos_calc(pos1, pos2, coefficient):
    pos_value = []
    for x1, x2 in zip(pos1, pos2):
        pos_value.append(x1 + ((x2 - x1) * coefficient))
    return pos_value


def binary_search(pos):
    epsilon = 10 ** -9
    left = 0
    right = 1.0
    left_pos = pos[0]
    right_pos = pos[1]
    dot_pos = pos[2]
    while abs(left - right) > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        mid1_pos = pos_calc(left_pos, right_pos, mid1)
        mid2_pos = pos_calc(left_pos, right_pos, mid2)
        dist1 = distance(mid1_pos, dot_pos)
        dist2 = distance(mid2_pos, dot_pos)
        if dist1 > dist2:
            left = mid1
        else:
            right = mid2
    mid_pos = pos_calc(left_pos, right_pos, (left + right) / 2)
    return distance(dot_pos, mid_pos)


def main():
    temp_pos = [int(x) for x in read().split()]
    pos = []
    for index in range(3):
        temp = []
        for j in range(DIMENSION):
            temp.append(temp_pos[index * DIMENSION + j])
        pos.append(tuple(temp))
    print(f'{binary_search(pos):0.9f}')


if __name__ == '__main__':
    main()
