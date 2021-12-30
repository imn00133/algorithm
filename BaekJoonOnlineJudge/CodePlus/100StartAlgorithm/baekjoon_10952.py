# https://www.acmicpc.net/problem/10952
# Solving Date: 20.03.19.

while True:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    else:
        print(a+b)
