# https://www.acmicpc.net/problem/11021
# Solving Date: 20.03.19.

test_case_num = int(input())
for count in range(1, test_case_num+1):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(count, a+b))
# range 시작을 바꾸지 말고, count+1을 해도 된다.
