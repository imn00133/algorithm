# https://www.acmicpc.net/problem/2292
# Solved Date: 20.04.08.
# fast 참고
# https://www.acmicpc.net/source/18997110


def fast_calc(num):
    shell = 0
    shell_num = 1
    while True:
        if num <= shell_num:
            print(shell + 1)
            break
        shell += 1
        shell_num += 6 * shell


def all_num(num):
    i = 0
    while True:
        if num == 1:
            print(1)
            break
        if 3 * i * (i + 1) + 1 < num <= 3 * (i + 1) * (i + 2) + 1:
            print(i + 2)
            break
        i += 1


def main():
    num = int(input())
    fast_calc(num)


if __name__ == '__main__':
    main()
