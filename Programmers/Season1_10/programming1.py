def convert_ten_base(three_base):
    answer = 0
    for i in range(len(three_base)):
        digit = len(three_base) - i - 1
        answer += three_base[i] * (3 ** digit)
    return answer


def convert_three_base(n):
    arr = []
    while n != 0:
        arr.append(n % 3)
        n = n // 3
    return arr


def solution(n):
    three_base = convert_three_base(n)
    answer = convert_ten_base(three_base)
    return answer


if __name__ == "__main__":
    print(solution(45))
    print(solution(125))
