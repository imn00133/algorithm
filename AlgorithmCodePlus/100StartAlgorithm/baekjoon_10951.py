# https://www.acmicpc.net/problem/10951
# Solving Date: 20.03.19.
# 끝을 모를 경우, EOF를 마지막에 입력받는다.
# 처리방법은 두 가지임으로 https://dodo4513.github.io/2017/07/02/python_algorithm/를 참고한다.
# sys.stdin.readline()이 더 빠르다고 하는데, 이는 확인해봐야 될 듯하다.
# 참고 https://enjoyso.tistory.com/10

while True:
	try:
		a, b = map(int, input().split())
		print(a+b)
	except EOFError:
		break
