# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
# Solved Date: 20.04.05.

import sys
read = sys.stdin.readline


def convert(s):
    nesting_depth = []
    end_digit = 0
    # compare digit to end_digit to make parentheses
    for digit in s:
        if digit > end_digit:
            for _ in range(digit - end_digit):
                nesting_depth.append('(')
            nesting_depth.append(str(digit))
            end_digit = digit
        elif digit < end_digit:
            for _ in range(end_digit - digit):
                nesting_depth.append(')')
            nesting_depth.append(str(digit))
            end_digit = digit
        else:
            nesting_depth.append(str(digit))
    # for close all parentheses
    for _ in range(end_digit):
        nesting_depth.append(')')
    return ''.join(nesting_depth)


def main():
    test_case_num = int(read().strip())
    for test_case in range(1, test_case_num+1):
        s = [int(x) for x in list(read().strip())]
        nesting_depth = convert(s)
        print("Case #{}: {}".format(test_case, nesting_depth))


if __name__ == '__main__':
    main()
