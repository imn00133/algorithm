# https://www.acmicpc.net/problem/15651
# Solved Date: 20.04.12.


def solved(n, m, ans):
    if m == 0:
        print(' '.join(ans))
        return 0
    for number in range(1, n+1):
        ans.append(str(number))
        solved(n, m-1, ans)
        ans.pop()
    return 0


def main():
    n, m = (int(x) for x in input().split())
    ans = []
    solved(n, m, ans)


if __name__ == '__main__':
    main()
