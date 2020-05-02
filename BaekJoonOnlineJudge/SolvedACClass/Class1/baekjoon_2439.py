# https://www.acmicpc.net/problem/2439
# Solving Date: 20.03.27.

num = int(input())
for i in range(num):
	print(' ' * (num - (i+1)), end='')
	print('*' * (i+1))
