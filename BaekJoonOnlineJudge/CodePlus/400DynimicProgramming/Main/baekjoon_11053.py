# https://www.acmicpc.net/problem/11053
# Solved Date: 20.04.01.
# 메모리 사용량을 줄이기 위해 tuple 생성
# 재귀 방식은 해결하지 못함

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
dp_arr = [0 for _ in range(MAX+1)]
dp_check = [False for _ in range(MAX+1)]


def bottom_up(sequence):
	for index, value in enumerate(sequence):
		dp_arr[index] = 1
		for sub_index in range(index):
			if sequence[sub_index] < value and dp_arr[sub_index] + 1 > dp_arr[index]:
				dp_arr[index] = dp_arr[sub_index] + 1


def top_down(sequence):
	if len(sequence) == 1:
		return 1
	if dp_check[len(sequence)-1]:
		return dp_arr[len(sequence)-1]
	for i in range(len(sequence)):
		if dp_arr[len(sequence)-1] == 0:
			dp_arr[len(sequence)-1] = 1
		if sequence[i] < sequence[len(sequence)-1] or top_down(sequence[:-1]) + 1 > dp_arr[len(sequence)-1]:
			dp_arr[len(sequence)-1] = top_down(sequence[:-1]) + 1
	dp_check[len(sequence)-1] = True
	return dp_arr[len(sequence)-1]


def main(mode=''):
	arr_len = int(read().strip())
	sequence = tuple([int(x) for x in read().split()])
	if mode == 'top':
		top_down(sequence)
	else:
		bottom_up(sequence)
	print(max(dp_arr[:len(sequence)]))


if __name__ == '__main__':
	main('top')
