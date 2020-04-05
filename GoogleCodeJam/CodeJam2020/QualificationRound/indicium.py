# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0
# Solved Date:


def make_array(n):
    arr = []
    line = [int(x) for x in range(1, n + 1)]
    for index in range(n):
        new_line = line[index:] + line[:index]
        arr.append(new_line)
    return arr


def swap_array(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def check_indicum(arr, k):
    trace = 0
    for i in range(len(arr)):
        trace += arr[i][i]
    if trace == k:
        return True
    else:
        return False


def arr_print(arr):
    for line in arr:
        for value in line:
            print(value, end=' ')
        print()


def main():
    test_case_num = int(input())
    for test_case in range(1, test_case_num + 1):
        n, k = [int(x) for x in input().split()]
        arr = make_array(n)
        flag_indcium = False
        if check_indicum(arr, k):
            flag_indcium = True
        for i in range(n-1):
            if flag_indcium:
                break
            for j in range(i+1, n):
                arr = swap_array(arr, i, j)
                if check_indicum(arr, k):
                    flag_indcium = True
                    break
                arr = swap_array(arr, i, j)
        if flag_indcium:
            print("Case #{}: POSSIBLE".format(test_case))
            arr_print(arr)
        else:
            print("CASE #{}: IMPOSSIBLE".format(test_case))


if __name__ == '__main__':
    main()
