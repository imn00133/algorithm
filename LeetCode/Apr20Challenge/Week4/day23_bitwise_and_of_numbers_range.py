# https://leetcode.com/problems/bitwise-and-of-numbers-range
# Solved Date: 20.04.23.
# diary의 20.04.23.를 참고한다.


def range_bitwise_and(m, n):
    number_count = n - m
    bit_num = 0
    while True:
        if (1 << bit_num) >= number_count:
            break
        bit_num += 1
    bitwise = m & n & ~((1 << bit_num) - 1)
    return bitwise


def main():
    m, n = (int(x) for x in input().split())
    print(range_bitwise_and(m, n))


if __name__ == '__main__':
    main()
