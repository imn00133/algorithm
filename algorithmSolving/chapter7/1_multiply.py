"""
chapter7의 도입에 있는 곱셈 프로그램 구현
O(n^2)과 O(n^log3)의 속도, 일반적인 python의 곱셈 속도도 비교
input, output을 normalize하는 시간은 포함하지 않았다.

time을 통한 속도 비교(decorator사용)
https://m.blog.naver.com/cjh226/221392127142
https://jeongukjae.github.io/posts/python%EC%97%90%EC%84%9C-%EC%8B%9C%EA%B0%84%EC%B8%A1%EC%A0%95%ED%95%98%EA%B8%B0/

timeit 참고사이트(코드가 너무 길어져서 사용 안함)
https://devluna.blogspot.com/2015/09/python-code-timeit.html
https://docs.python.org/ko/3/library/timeit.html

곱샘프로그램의 입출력은 각 수의 자릿수가 1의 자리에서부터 시작해서 저장
ex) 1multiply([3, 2, 1], [6, 5, 4] = 123 * 456 = 56088 = [8, 8, 0, 6, 5]
"""
import time
import string
import random


def logging_time(original_fn):
	def wrapper_fn(*args, **kwargs):
		start_time = time.time()
		result = original_fn(*args, **kwargs)
		end_time = time.time()
		print("Working Time[{0}]: {1:.10f} sec".format(original_fn.__name__, end_time - start_time))
		return result
	return wrapper_fn


def random_num(digit=6):
	"""
	자리수만큼의 숫자 랜덤 제작
	:param digit: 자리수
	:return result: string로 구성된 숫자
	"""
	# https://hongku.tistory.com/297
	result = ""
	result += random.choice(string.digits[1:])
	for _ in range(digit-1):
		result += random.choice(string.digits)
	return result


def input_normalize(num):
	num = " ".join(num).split()
	num.reverse()
	num = list(map(int, num))
	return num


def output_normalize(num):
	pass


def normalize(num):
	num.append(0)
	for i in range(len(num)):
		# karatsuba를 사용하기 위한 버림 계산
		if num[i] < 0:
			borrow = (abs(num[i]) + 9) / 10
			num[i+1] -= borrow
			num[i] += 10
		else:
			num[i+1] += num[i] / 10
			num[i] %= 10
	while True:
		if len(num) > 1 and num[-1] == 0:
			num.pop()


@logging_time
def multiply(num1, num2, loop=1):
	# 가장 큰 수를 더했을 때, 최대 크기는 각 자리수의 덧셈, +1은 왜 했을까?
	for _ in range(loop):
		ans = [0 for _ in range(len(num1)+len(num2)+1)]
		for i in range(len(num1)):
			for j in range(len(num2)):
				ans[i+j] += num1[i]+num2[j]
	normalize(ans)
	return ans


@logging_time
def python_multiply(num1, num2, loop=1):
	num1, num2 = int(num1), int(num2)
	ans = 0
	for _ in range(loop):
		ans = num1 * num2
	return ans


def init_value():
	# 클로저가 필요한데 포기. 대충 하자.
	digit = input("생성할 숫자 자리수를 입력하세요(기본값 6자리):")
	if digit == "":
		num = random_num()
	else:
		num = random_num(int(digit))
	return num


def main():
	# 1번으로는 시간이 계산되지 않아, 50000번 반복한다.
	loop = 50000
	num1 = init_value()
	print("생성된 숫자 1: " + num1)
	num2 = init_value()
	print("생성된 숫자 2: " + num2)
	py_mul = python_multiply(num1, num2, loop)
	num1 = input_normalize(num1)
	num2 = input_normalize(num2)
	on2_mul = multiply(num1, num2, loop)


if __name__ == "__main__":
	main()
