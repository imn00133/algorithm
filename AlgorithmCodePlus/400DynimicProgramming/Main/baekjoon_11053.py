# https://www.acmicpc.net/problem/11053
# Solved Date: 20.04.01.
# 재귀 방식은 해결하지 못함

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
dp_arr = [0 for _ in range(MAX+1)]


def bottom_up(sequence):
	for index, value in enumerate(sequence):
		dp_arr[index] = 1
		for sub_index in range(index):
			if sequence[sub_index] < value and dp_arr[sub_index] + 1 > dp_arr[index]:
				dp_arr[index] = dp_arr[sub_index] + 1


def top_down(index, sequence):
	if index == 0:
		dp_arr[index] = 1
		return dp_arr[index]
	if dp_arr[index] > 0:
		return dp_arr[index]
	for i in range(1, index):
		if sequence[i] < sequence[index]:
			dp_arr[index] = max(top_down(i-1, sequence) + 1, dp_arr[index])
	if dp_arr[index] == 0:
		dp_arr[index] = 1
	return dp_arr[index]


def main(mode=''):
	arr_len = int(read().strip())
	sequence = [int(x) for x in read().split()]
	if mode == 'top':
		top_down(len(sequence)-1, sequence)
	else:
		bottom_up(sequence)
	print(max(dp_arr[:len(sequence)]))


if __name__ == '__main__':
	main()
