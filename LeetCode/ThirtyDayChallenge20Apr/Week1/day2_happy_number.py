# https://leetcode.com/problems/happy-number/
# Solved Date 20.04.03.
# 이런 pythonic한 방법이 있다니...


def pythonic(n):
    SQUARES = tuple([i * i for i in range(10)])
    seen = set()
    while True:
        n = sum([SQUARES[int(x)] for x in str(n)])
        if n == 1:
            return True
        elif n in seen:
            return False
        else:
            seen.add(n)


def is_happy(n):
    squares = [i * i for i in range(10)]
    dp_arr = [False for _ in range(1000)]
    while True:
        if n == 1:
            return True
        temp = [int(x) for x in str(n)]
        temp.append(n)
        n = 0
        for value in temp[:-1]:
            n += squares[value]
        if temp[-1] <= 1000:
            dp_arr[temp[-1]] = True
        if dp_arr[n]:
            return False


def main():
    n = int(input())
    print(pythonic(n))


if __name__ == '__main__':
    main()
