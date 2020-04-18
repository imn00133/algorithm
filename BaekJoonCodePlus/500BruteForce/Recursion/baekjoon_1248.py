# https://www.acmicpc.net/problem/1248
# Solved Date: 20.04.17.

import sys
read = sys.stdin.readline


def check(index, arr, ans):
    acc = 0
    for i in range(index, -1, -1):
        sign = arr[i][index]
        acc += ans[i]
        if sign == 1 and acc <= 0:
            return False
        elif sign == -1 and acc >= 0:
            return False
        elif sign == 0 and acc != 0:
            return False
    return True


def recursive(num, arr, ans, index=0, flag=False):
    if index == len(ans):
        print(*ans)
        return True
    sign = arr[index][index]
    if sign:
        for number in range(1, 11):
            ans[index] = sign * number
            if not check(index, arr, ans):
                continue
            flag = recursive(num, arr, ans, index+1, flag)
            ans[index] = 0
            if flag:
                break
    else:
        flag = recursive(num, arr, ans, index+1, flag)
    return flag


def main():
    arr_num = int(read().strip())
    temp = []
    for letter in read().strip():
        if letter == '+':
            temp.append(1)
        elif letter == '-':
            temp.append(-1)
        else:
            temp.append(0)
    arr = []
    acc_index = 0
    for index in range(arr_num, 0, -1):
        next_index = acc_index + index
        arr.append([0 for _ in range(arr_num - index)] + temp[acc_index:next_index])
        acc_index = next_index
    ans = [0 for _ in range(arr_num)]
    recursive(arr_num, arr, ans)


if __name__ == '__main__':
    main()
