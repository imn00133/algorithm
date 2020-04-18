# https://www.acmicpc.net/problem/17298
# Solving Date: 20.03.25.

import sys
read = sys.stdin.readline


def solve(num_arr):
	solved_arr = [-1 for _ in range(len(num_arr))]
	stack = []
	for index, content in enumerate(num_arr):
		# 기저조건, stack이 비면, index를 넣는다. -> stack비교를 아래에서 함으로, 이 조건을 삭제해도 된다.
		# if not stack:
		#    stack.append(index)
		#    continue
		# 비어있지 않아야 함으로 비지 않도록 조건을 넣는다.
		while stack and num_arr[stack[-1]] < content:
			solved_arr[stack.pop()] = content
		stack.append(index)
	return solved_arr


def slow_solve(num_arr):
	solved_arr = []
	for index, content in enumerate(num_arr):
		flag_value = False
		for compare in num_arr[index:]:
			if content < compare:
				solved_arr.append(str(compare))
				flag_value = True
				break
		if not flag_value:
			solved_arr.append(str(-1))
	return solved_arr


def main(mode=''):
	array_max = int(read().strip())
	num_arr = [int(x) for x in read().split()]
	solved_arr = solve(num_arr)
	solved_arr = [str(x) for x in solved_arr]
	print(' '.join(solved_arr))


if __name__ == '__main__':
	main()
