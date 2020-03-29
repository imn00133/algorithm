# https://www.acmicpc.net/problem/2739
# Solving Date: 20.03.27.

num = int(input())
for i in range(1, 10):
	print("{num} * {i} = {calc}".format(num=num, i=i, calc=num*i))
