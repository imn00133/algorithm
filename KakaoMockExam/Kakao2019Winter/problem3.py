# Solving Date: 20.03.28.


def compare_id(individual_user_id, individual_banned_id):
    flag_same_id = True
    for i in range(len(individual_user_id)):
        if individual_banned_id[i] == '*':
            continue
        elif individual_user_id[i] != individual_banned_id[i]:
            flag_same_id = False
            break
    return flag_same_id


def user_id_list(user_id, individual_banned_id):
    add_block_id = []
    for individual_user_id in user_id:
        if len(individual_user_id) != len(individual_banned_id):
            continue
        if compare_id(individual_user_id, individual_banned_id):
            add_block_id.append(individual_user_id)
    return add_block_id


def combination_count(block_id, selected_id_list):
    ret = 0
    if not block_id:
        return 1
    for selected_id in block_id[0]:
        if selected_id in selected_id_list:
            continue
        selected_id_list.append(selected_id)
        ret += combination_count(block_id[1:], selected_id_list)
        selected_id_list.pop()
    return ret


def solution(user_id, banned_id):
    block_id = []
    for individual_banned_id in banned_id:
        block_id.append(user_id_list(user_id, individual_banned_id))
    if all(block_id):
        combination = combination_count(block_id, [])
    else:
        combination = 0
    return combination


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
