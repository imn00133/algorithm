# https://www.acmicpc.net/problem/1085
# Solved Date: 20.04.07.


def main():
    x, y, w, h = [int(x) for x in input().split()]
    print(min(x, y, w-x, h-y))


if __name__ == '__main__':
    main()
