# https://leetcode.com/problems/first-bad-version/
# Solved Date: 20.05.02.


def first_bad_version(n):
    start = 1
    end = n
    while True:
        if start == end:
            return start
        # overflow가 있는 언어의 경우 start + (end - start) // 2를 하여야 한다.
        mid = (start + end) // 2
        if is_bad_version(mid):
            end = mid
        else:
            start = mid + 1


def is_bad_version(version):
    first_bade_version = 4
    if version >= first_bade_version:
        return True
    else:
        return False


def main():
    print(first_bad_version(5))


if __name__ == '__main__':
    main()
