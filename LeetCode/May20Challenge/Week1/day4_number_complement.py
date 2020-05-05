# https://leetcode.com/problems/number-complement/
# Solved Date: 20.05.05.


def find_complement(num):
    index = 1
    while num >= (1 << index):
        index += 1
    ans = num ^ ((1 << index) - 1)
    return ans


def main():
    print(find_complement(0))
    print(find_complement(1))
    print(find_complement(5))
    print(find_complement(2))
    print(find_complement(8))


if __name__ == '__main__':
    main()
