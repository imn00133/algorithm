# https://www.acmicpc.net/problem/2743
# Solving Date: 20.03.29.
# 오차범위내로 같다..?


def legacy_len(string):
    count = 0
    for _ in range(len(string)):
        count += 1
    return count


def pythonic_len(string):
    return len(string)


def main():
    string = input()
    print(pythonic_len(string))


if __name__ == '__main__':
    main()
