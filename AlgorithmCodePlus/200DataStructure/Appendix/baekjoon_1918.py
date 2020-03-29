# https://www.acmicpc.net/problem/1918
# Solving Date: 20.03.27.

import sys


def operation(value, operator_stack, postfix_expression):
	# 스택 내에 있을 수 있는 경우의 수는 +(-) or +* or *(/)만 가능하다.
	# 들어오는 연산자는 +-*/만이다
	# '('가 앞에 있을 수 있으니, 이 때도 출력을 제외한다.
	if value in '+-' and operator_stack[-1] != '(':
		postfix_expression.append(operator_stack.pop())
		if operator_stack and operator_stack[-1] in '+-':
			postfix_expression.append(operator_stack.pop())
	# 그 외의 value는 */임으로, 마지막이 */일 때만 고려한다.
	elif operator_stack[-1] in '*/':
		postfix_expression.append(operator_stack.pop())
	operator_stack.append(value)


def convert_postfix(expression):
	postfix_expression = []
	operator_stack = []
	for value in expression:
		if ord('A') <= ord(value) <= ord('Z'):
			postfix_expression.append(value)
		# 기저조건: 비어있거나, (를 만났을 때
		elif not operator_stack or value == '(':
			operator_stack.append(value)
		elif value == ')':
			while operator_stack[-1] != '(':
				postfix_expression.append(operator_stack.pop())
			# '('를 제거
			operator_stack.pop()
		else:
			operation(value, operator_stack, postfix_expression)
	while operator_stack:
		postfix_expression.append(operator_stack.pop())
	postfix_expression = ''.join(postfix_expression)
	return postfix_expression


def main(mode=''):
	read = sys.stdin.readline
	file = None
	if mode == 'f':
		file = open("baekjoon_1918_input.txt", mode='r', encoding='utf-8')
		read = file.readline
	expression = list(read().strip())
	print(convert_postfix(expression))
	if mode == 'f':
		file.close()


if __name__ == '__main__':
	main()
