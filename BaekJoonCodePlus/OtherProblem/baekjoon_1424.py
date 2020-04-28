# https://www.acmicpc.net/problem/1424
# Solved Date: 20.04.28.

import sys
read = sys.stdin.readline


def main():
    number = int(read().strip())
    length = int(read().strip())
    capacity = int(read().strip())

    count = capacity // (length + 1)
    if capacity % (length + 1) == length:
        count += 1

    if count % 13 == 0:
        count -= 1

    cd_count = number // count
    if number % count > 0:
        cd_count += 1

    print(cd_count)


if __name__ == '__main__':
    main()
