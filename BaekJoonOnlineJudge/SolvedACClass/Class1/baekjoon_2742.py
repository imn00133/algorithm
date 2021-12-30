# https://www.acmicpc.net/problem/2742
# Solving Date: 20.03.28.


def used_reverse_range(num):
    for index in range(num, 0, -1):
        print(index)


def not_used_range(num):
    for index in range(1, num+1):
        print(num+1 - index)


def main():
    num = int(input())
    used_reverse_range(num)


if __name__ == '__main__':
    main()
