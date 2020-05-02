# https://www.acmicpc.net/problem/15652
# Solved Date: 20.04.12.


def solved(n, m, ans, start=1):
    if m == 0:
        print(' '.join(ans))
        return 0
    for number in range(start, n+1):
        ans.append(str(number))
        solved(n, m-1, ans, number)
        ans.pop()


def main():
    n, m = (int(x) for x in input().split())
    ans = []
    solved(n, m, ans)


if __name__ == '__main__':
    main()
