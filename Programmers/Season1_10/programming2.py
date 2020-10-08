def divide_arr(arr, arr_len, left):
    new_arr = []
    if left:
        for row in arr:
            new_arr.append(row[:arr_len])
    else:
        for row in arr:
            new_arr.append(row[arr_len:])
    return new_arr


def recursion(arr):
    if len(arr) == 1:
        if arr[0][0]:
            return [0, 1]
        else:
            return [1, 0]
    arr_len = len(arr) // 2
    left_up = recursion(divide_arr(arr[:arr_len], arr_len, True))
    left_down = recursion((divide_arr(arr[arr_len:], arr_len, True)))
    right_up = recursion(divide_arr(arr[:arr_len], arr_len, False))
    right_down = recursion((divide_arr(arr[arr_len:], arr_len, False)))
    value = zip(left_up, right_up, right_down, left_down)
    value = [sum(temp) for temp in value]
    if value[0] == 4 and value[1] == 0:
        return [1, 0]
    elif value[0] == 0 and value[1] == 4:
        return [0, 1]
    else:
        return value


def solution(arr):
    return recursion(arr)


if __name__ == '__main__':
    arr = [[1, 1, 0, 0],
           [1, 0, 0, 0],
           [1, 0, 0, 1],
           [1, 1, 1, 1]]
    print(solution(arr))
    arr = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 1, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 1, 1]]
    print(solution(arr))
