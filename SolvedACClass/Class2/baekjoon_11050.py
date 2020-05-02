# https://www.acmicpc.net/problem/11050
# Solved Date: 20.04.12.


def factorial(num, end=0):
    if num == end:
        return 1
    return num * factorial(num-1, end)


def binomial_coefficient(n, k):
    return factorial(n, n-k) // factorial(k)


def main():
    n, k = (int(x) for x in input().split())
    print(binomial_coefficient(n, k))


if __name__ == '__main__':
    main()
