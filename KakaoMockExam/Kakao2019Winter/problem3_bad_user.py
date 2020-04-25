# https://programmers.co.kr/learn/courses/30/lessons/64064
# Solving Date: 20.04.26.


def compare_str(user, banned):
    if len(user) != len(banned):
        return False
    for index in range(len(user)):
        if banned[index] == '*':
            continue
        elif user[index] != banned[index]:
            return False
    return True


def compare_id(user_id, banned):
    block_id = []
    for user in user_id:
        if compare_str(user, banned):
            block_id.append(user)
    return block_id


def id_count(block_id, ans, whole_ans, index=0):
    if len(ans) == len(block_id):
        temp = ans.copy()
        whole_ans.append(temp)
        return 1
    elif len(block_id) == index:
        return 0
    count = 0
    for block in block_id[index]:
        if block in ans:
            continue
        ans.append(block)
        count += id_count(block_id, ans, whole_ans, index+1)
        ans.pop()
    return count


def solution(user_id, banned_id):
    block_id = [[] for _ in range(len(banned_id))]
    for index in range(len(banned_id)):
        block_id[index].extend(compare_id(user_id, banned_id[index]))

    # 하나라도 불량 id가 없을 경우 목록은 0이 된다.
    if not all(block_id):
        return 0

    ans = []
    whole_ans = []
    id_count(block_id, ans, whole_ans)
    tuple_ans = []
    for ans in whole_ans:
        tuple_ans.append(tuple(sorted(ans)))
    whole_ans = set(tuple_ans)
    return len(whole_ans)


def main():
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))


if __name__ == '__main__':
    main()
