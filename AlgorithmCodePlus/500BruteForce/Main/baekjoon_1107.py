# https://www.acmicpc.net/problem/1107
# Solved Date: 20.04.04.
# 반례 참조 https://www.acmicpc.net/board/view/46120

import sys
read = sys.stdin.readline


MAX = 1000000


def make_close_num(target, un_broken_nums):
    close_num_list = []
    # 각 자리마다 고장나지 않은 버튼의 값 중 차이가 가장 적은 것을 찾아 가장 가까운 값을 반환
    while True:
        remainder = target % 10
        target //= 10
        diff_num = 10
        close_temp_num = 0
        for value in un_broken_nums:
            if abs(remainder - value) < diff_num:
                close_temp_num = value
                diff_num = abs(remainder - value)
        close_num_list.append(close_temp_num)
        if target == 0:
            break
    close_num = 0
    for index in range(len(close_num_list)):
        close_num += close_num_list[index] * (10 ** index)
    return close_num


def compare(target, broken_nums):
    # Failed: 고려해야되는 방법이 너무 많아 포기
    min_count = MAX // 2
    # 가장 가까운 숫자를 찾아 그 때 누르는 버튼 숫자를 구한다.
    if len(broken_nums) != 10:
        un_broken_nums = [x for x in range(10) if x not in broken_nums]
        # 전체 자리에 대한 가장 가까운 값
        close_num = make_close_num(target, un_broken_nums)
        min_count = min(min_count, abs(close_num - target) + len(str(close_num)))
    min_count = min(min_count, abs(target - 100))
    return min_count


def check_make_num(select_num, broken_nums):
    # broken_num에 들어간 값이 있는지 확인하여 있으면 False를 반환
    flag = True
    for value in select_num:
        if value in broken_nums:
            flag = False
    return flag


def brute_force(target, broken_nums):
    min_count = MAX // 2
    # 처음부터 끝까지 다 골라서 하기
    for select_num in range(MAX+1):
        select_num_text = str(select_num)
        select_count = 0
        if check_make_num(select_num_text, broken_nums):
            select_count += len(select_num_text)
            select_count += abs(select_num - target)
            min_count = min(min_count, select_count)
    # 100에서 이동하는 경우의 수
    min_count = min(min_count, abs(target-100))
    return min_count


def main(mode=''):
    target = int(read().strip())
    broken_count = int(read().strip())
    broken_nums = [int(x) for x in read().split()]
    if mode == 'brute':
        broken_nums = [str(x) for x in read().split()]
        min_count = brute_force(target, broken_nums)
    else:
        min_count = compare(target, broken_nums)
    print(min_count)


if __name__ == '__main__':
    main()
