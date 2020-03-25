# https://www.acmicpc.net/problem/17299

import sys
read = sys.stdin.readline


def solve(num_arr):
	# 1,000,000이 들어가기 위해서는 1이 포함되어야 한다.
	freq_arr = [0 for _ in range(1000001)]
	for index in num_arr:
		freq_arr[index] += 1
	ans_arr = [-1 for _ in range(len(num_arr))]
	stack = []
	for index, content in enumerate(num_arr):
		while stack and freq_arr[num_arr[stack[-1]]] < freq_arr[content]:
			ans_arr[stack.pop()] = content
		stack.append(index)
	return ans_arr


def main(mode=''):
	arr_num = 0
	num_arr = []
	if mode == 'f':
		file = open('baekjoon_17299_input.txt', mode='r', encoding='utf-8')
		arr_num = int(file.readline().strip())
		num_arr = file.readline().split()
	else:
		arr_num = int(read().strip())
		num_arr = read().split()
	num_arr = [int(x) for x in num_arr]
	ans_arr = solve(num_arr)
	ans_arr = [str(x) for x in ans_arr]
	print(' '.join(ans_arr))


if __name__ == '__main__':
	main()
