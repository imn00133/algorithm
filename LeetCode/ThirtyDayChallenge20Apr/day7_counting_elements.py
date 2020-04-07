#
# Solved Date: 20.04.07.


def count_elements(arr):
    count_dict = {}
    for number in arr:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    count = 0
    for key, value in count_dict.items():
        if key+1 in count_dict:
            count += value
    return count


def main():
    while True:
        arr = [int(x) for x in input().split()]
        if not arr or arr[0] == -1:
            break
        print(count_elements(arr))


if __name__ == '__main__':
    main()
