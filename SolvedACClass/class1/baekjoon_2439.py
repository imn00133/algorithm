# https://www.acmicpc.net/problem/2439

num = int(input())
for i in range(num):
	print(' ' * (num - (i+1)), end='')
	print('*' * (i+1))
