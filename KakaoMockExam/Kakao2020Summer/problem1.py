#
# Solved Date: 20.05.09.

# 0에서 9까지 위치 (y, x)
NUMBER_POS = ((3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))


def rel_distance(hand_pos, number):
    total = 0
    for hand_value, phone_value in zip(hand_pos, NUMBER_POS[number]):
        total += abs(hand_value - phone_value)
    return total


def add_answer(ans, direction, number):
    if direction == 'left':
        ans.append('L')
    else:
        ans.append('R')
    return NUMBER_POS[number]


def solution(numbers, hand):
    left_pos = (3, 0)
    right_pos = (3, 2)
    answer = []
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            left_pos = add_answer(answer, 'left', number)
        elif number == 3 or number == 6 or number == 9:
            right_pos = add_answer(answer, 'right', number)
        else:
            left_distance = rel_distance(left_pos, number)
            right_distance = rel_distance(right_pos, number)
            if left_distance > right_distance:
                right_pos = add_answer(answer, 'right', number)
            elif left_distance < right_distance:
                left_pos = add_answer(answer, 'left', number)
            else:
                if hand == 'left':
                    left_pos = add_answer(answer, 'left', number)
                else:
                    right_pos = add_answer(answer, 'right', number)
    return ''.join(answer)


def main():
    numbers = []
    hand = ""
    print(solution(numbers, hand))


if __name__ == '__main__':
    main()
