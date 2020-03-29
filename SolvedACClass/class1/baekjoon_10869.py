# https://www.acmicpc.net/problem/10869
# Solving Date: 20.03.26.

import sys
read = sys.stdin.readline

a, b = (int(x) for x in read().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
