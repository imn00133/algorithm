#
# Solved Date: 20.04.15.


def string_shift(s, shift):
    index = 0
    for flag, shift_num in shift:
        # flag가 0이면, 자동으로 False로 취급된다.
        if flag == 0:
            index += shift_num
        else:
            index -= shift_num
    # 그냥 %= len(s)를 하면, 원하는 index가 나온다.
    if index > 0:
        index = index % len(s)
    else:
        index = ((index + 1) % len(s)) - 1
    return s[index:] + s[:index]


def main():
    s = "mecsk"
    shift = [[1, 4], [0, 5], [0, 4], [1, 1], [1, 5]]
    print(string_shift(s, shift))


if __name__ == '__main__':
    main()
