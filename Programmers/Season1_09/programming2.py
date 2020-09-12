def make_answer(array):
    answer = []
    for i in range(len(array)):
        for j in range(i + 1):
            answer.append(array[i][j])
    return answer


def solution(n):
    array = [[0 for _ in range(n)] for _ in range(n)]
    y, x = 0, 0
    state = 0
    step = n - 1
    number = 1
    end = n * (n + 1) // 2
    while number < end:
        for _ in range(step):
            array[y][x] = number
            number += 1
            if state % 3 == 0:
                y += 1
            elif state % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1
        state += 1
        step -= 1
        array[y][x] = number
        number += 1
        if state % 3 == 0:
            y += 1
        elif state % 3 == 1:
            x += 1
        else:
            y -= 1
            x -= 1
    array[y][x] = number
    answer = make_answer(array)
    return answer


if __name__ == "__main__":
    n = 5
    print(solution(n))
