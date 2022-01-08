#
# Solved Date: 20.05.09.


def operator(num1, num2, op):
    if op == '*':
        number = num1 * num2
    elif op == '+':
        number = num1 + num2
    else:
        number = num1 - num2
    return number


def priority_value(op, priority):
    if op == '*':
        return priority[0]
    elif op == '+':
        return priority[1]
    else:
        return priority[2]


def calc(expression, priority):
    # priority 순서는 *, +, -이고 작을수록 우선순위가 높다.
    num_stack = [expression[0]]
    op_stack = []
    for index in range(1, len(expression), 2):
        if op_stack:
            cur_op = expression[index]
            while op_stack:
                prev_op = op_stack.pop()
                prev_op_priority = priority_value(prev_op, priority)
                cur_op_priority = priority_value(cur_op, priority)
                if prev_op_priority <= cur_op_priority:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(operator(num1, num2, prev_op))
                else:
                    op_stack.append(prev_op)
                    break
            op_stack.append(cur_op)
            num_stack.append(expression[index+1])
        else:
            op_stack.append(expression[index])
            num_stack.append(expression[index+1])
    while op_stack:
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(operator(num1, num2, op_stack.pop()))
    return num_stack[0]


def parsing(expression):
    change_expression = []
    pre_index = 0
    for index in range(len(expression)):
        if expression[index] in '*+-':
            change_expression.append(int(expression[pre_index:index]))
            change_expression.append(expression[index])
            pre_index = index + 1
    change_expression.append(int(expression[pre_index:]))
    return change_expression


def solution(expression):
    expression = parsing(expression)
    answer = 0
    from itertools import permutations
    for priority in permutations((0, 1, 2)):
        answer = max(abs(calc(expression, priority)), answer)
    return answer


def main():
    expression = "50*6-3*2"
    print(solution(expression))


if __name__ == '__main__':
    main()
