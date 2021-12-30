# https://www.acmicpc.net/problem/1330
# Solving Date: 20.03.27.

a, b = (int(x) for x in input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
