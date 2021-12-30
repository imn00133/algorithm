# https://www.acmicpc.net/problem/11021
# Solving Date: 20.03.19.

test_case_num = int(input())
for count in range(test_case_num):
    # a, b = (int(x) for x in test_case_num.split())도 가능하다.
    # 리스트 내포, 제너레이트 둘 다 가능.
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(count+1, a, b, a+b))
