#
# Solved Date: 20.05.09.


def solution(gems):
    having_gem = {}
    for gem in gems:
        if gem not in having_gem:
            having_gem[gem] = 0
    kind_num = len(having_gem.keys())
    current_num = 0
    pre_index = 0
    candidate = (0, len(gems))
    for index in range(len(gems)):
        gem = gems[index]
        if having_gem[gem] == 0:
            current_num += 1
        having_gem[gem] += 1
        if kind_num == current_num:
            candidate_len = candidate[1] - candidate[0]
            if candidate_len > index - pre_index:
                candidate = (pre_index + 1, index + 1)
        while having_gem[gems[pre_index]] > 1:
            having_gem[gems[pre_index]] -= 1
            pre_index += 1
            if pre_index > index:
                break
    return list(candidate)


def main():
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))


if __name__ == '__main__':
    main()
