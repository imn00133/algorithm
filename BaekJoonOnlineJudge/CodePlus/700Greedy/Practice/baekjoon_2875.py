# https://www.acmicpc.net/problem/2875
# Solved Date: 20.05.20.

import sys
read = sys.stdin.readline


def main():
    woman, man, inter_ship = (int(x) for x in read().split())
    print(min((woman + man - inter_ship) // 3, woman // 2, man))


if __name__ == '__main__':
    main()
