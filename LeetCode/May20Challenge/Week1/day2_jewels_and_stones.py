# https://leetcode.com/problems/jewels-and-stones/
# Solved date: 20.05.03.


def fast_num_jewels_in_stones(J, S):
    count_dict = {}
    for stone in S:
        if stone in count_dict:
            count_dict[stone] += 1
        else:
            count_dict[stone] = 1
    count = 0
    for jewel in J:
        if jewel in count_dict:
            count += count_dict[jewel]
    return count


def num_jewels_in_stones(J: str, S: str) -> int:
    count = 0
    for jewel in J:
        for stone in S:
            if jewel == stone:
                count += 1
    return count


def main():
    print(fast_num_jewels_in_stones("aA", "aAAbbbb"))


if __name__ == '__main__':
    main()
