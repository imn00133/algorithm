# https://www.acmicpc.net/problem/2133
# Solved Date: 20.04.09.

MAX = 30
dp_arr = [0 for _ in range(MAX+1)]


def bottom_up(num):
    dp_arr[0] = 1
    for i in range(2, num+1, 2):
        dp_arr[i] += 3 * dp_arr[i-2]
        for j in range(4, i+1, 2):
            dp_arr[i] += 2 * dp_arr[i-j]
    return dp_arr[num]


def main():
    num = int(input())
    print(bottom_up(num))


if __name__ == '__main__':
    main()
