# O(n^3)으로 풀었는데.. 더 빠른 방법이 있지 않을까.
# 중간 중간에 검사하는게 더 빠를 수 있을 것 같다.


def convert_list(s):
    # 문자열을 읽고 이중 리스트를 반환한다.
    sorted_list = []
    start_index = 0
    sub_s = s[1:-1]
    for index, letter in enumerate(sub_s):
        if letter == '{':
            start_index = index + 1
        elif letter == '}':
            sorted_list.append([int(x) for x in sub_s[start_index:index].split(',')])
            # sort는 key에 함수를 주어, 원하는 대로 정렬할 수 있다.
            sorted_list.sort(key=len)
    return sorted_list


def solution(s):
    result_list = []
    sorted_list = convert_list(s)
    for inner_list in sorted_list:
        for value in inner_list:
            if value not in result_list:
                result_list.append(value)
                break
    return result_list
