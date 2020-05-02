# https://www.acmicpc.net/problem/2529
# Solved Date: 20.05.02.

import sys
import itertools

read = sys.stdin.readline


def check_inequality(sign, ans_num, select_num):
    if (sign == '<' and ans_num < select_num) or \
            (sign == '>' and ans_num > select_num):
        return True
    else:
        return False


def recursion(inequality, num_list, ans, check, flag=False):
    if len(ans) > len(inequality):
        for number in ans:
            print(number, end='')
        print()
        return True
    for index in range(len(num_list)):
        if flag:
            return True
        if check[index]:
            continue
        select_num = num_list[index]
        if len(ans) == 0 or check_inequality(inequality[len(ans)-1], ans[-1], select_num):
            ans.append(select_num)
        else:
            return False
        check[index] = True
        flag = recursion(inequality, num_list, ans, check, flag)
        ans.pop()
        check[index] = False
    return flag


def permutation(inequality, num_list):
    ans = []
    ans_length = len(inequality) + 1
    for list_permutation in itertools.permutations(num_list, ans_length):
        ans.clear()
        ans.append(list_permutation[0])
        for index in range(len(list_permutation) - 1):
            ans_num = ans[index]
            select_num = list_permutation[index+1]
            if not check_inequality(inequality[index], ans_num, select_num):
                break
            else:
                ans.append(select_num)
        if len(ans) == ans_length:
            break
    return ans


def main(mode=''):
    num = int(read().strip())
    inequality = read().split()
    num_list = [int(x) for x in range(9, -1, -1)]
    if mode == 'permutation':
        print(*permutation(inequality, num_list), sep='')
        num_list.reverse()
        print(*permutation(inequality, num_list), sep='')
    else:
        ans = []
        check = [False for _ in range(10)]
        # 최대 값을 구하고, flag를 통해 종료한다.
        recursion(inequality, num_list, ans, check)
        num_list.reverse()
        # 최소 값을 구한다.
        recursion(inequality, num_list, ans, check)


if __name__ == '__main__':
    main('permutation')
