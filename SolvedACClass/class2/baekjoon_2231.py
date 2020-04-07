# https://www.acmicpc.net/problem/2231
# Solved Date: 20.04.07.
# fast참고
# https://itadventure.tistory.com/158


def fast_brute_force(num):
    temp = str(num)
    start_num = num - len(temp) * 9
    if start_num < 0:
        start_num = 0
    for number in range(start_num, num):
        decomp = number + sum([int(x) for x in list(str(number))])
        if decomp == num:
            print(number)
            break
        elif number == num-1:
            print(0)


def brute_force(num):
    for i in range(0, num):
        decomp = i + sum([int(x) for x in list(str(i))])
        if decomp == num:
            print(i)
            break
        elif i == num-1:
            print(0)


def main(mode=''):
    num = int(input())
    if mode == 'brute':
        brute_force(num)
    else:
        fast_brute_force(num)


if __name__ == '__main__':
    main()
