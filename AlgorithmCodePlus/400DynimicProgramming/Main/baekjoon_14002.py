# https://www.acmicpc.net/problem/14002
# Solved Date: 20.04.01.
# 유사한 11053 재귀도 해결하지 못하였음으로, 재귀는 넘어간다.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
# dp_arr[i][j], i는 수열의 길이, j는 이전 index
dp_arr = [[0, 0] for _ in range(MAX+1)]


def bottom_up(sequence):
	for index, value in enumerate(sequence):
		dp_arr[index][0] = 1
		dp_arr[index][1] = index
		for sub_index in range(index):
			if sequence[sub_index] < value and dp_arr[sub_index][0] + 1 > dp_arr[index][0]:
				dp_arr[index][0] = dp_arr[sub_index][0] + 1
				dp_arr[index][1] = sub_index


def find_sequence(sequence, lis, index):
	if dp_arr[index][0] == 1:
		return lis.append(sequence[index])
	find_sequence(sequence, lis, dp_arr[index][1])
	return lis.append(sequence[index])


def top_down(sequence):
	pass


def main(mode=''):
	arr_num = int(read().strip())
	sequence = [int(x) for x in read().split()]
	if mode == 'top':
		top_down(sequence)
	else:
		bottom_up(sequence)
		max_index = 0
		for index, lis_value in enumerate(dp_arr[:arr_num]):
			if lis_value[0] > dp_arr[max_index][0]:
				max_index = index
		print(dp_arr[max_index][0])

		# 최대 길이 수열 반환
		lis = []
		find_sequence(sequence, lis, max_index)
		for value in lis:
			print(value, end=' ')


if __name__ == '__main__':
	main()
