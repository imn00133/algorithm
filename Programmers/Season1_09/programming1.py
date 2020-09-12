def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = sorted(list(answer))
    return answer


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 1]
    print(solution(numbers))
