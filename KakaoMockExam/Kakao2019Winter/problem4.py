# Solving Date: 20.03.28.


def solution(k, room_number):
    # 효율성 테스트 실패
    room_full = [False for x in range(k+1)]
    assign_room = []
    for ask_room in room_number:
        while room_full[ask_room]:
            ask_room += 1
        room_full[ask_room] = True
        assign_room.append(ask_room)
    return assign_room


def solution2(k, room_number):
    # room_full은 방이 비었는지 확인하는 변수
    # room_move_pos는 차있을 경우, 이동할 위치를 저장하는 변수
    # 런타임 에러가 있...
    # 결국 효율성은 0이다.
    room_full = [False for _ in range(k+1)]
    room_move_pos = [0 for _ in range(k+1)]
    assign_room = []
    for ask_room in room_number:
        pos_assigned = 0
        if not room_full[ask_room]:
            room_full[ask_room] = True
            assign_room.append(ask_room)
            pos_assigned = ask_room
        else:
            room_full[room_move_pos[ask_room]] = True
            assign_room.append(room_move_pos[ask_room])
            pos_assigned = room_move_pos[ask_room]
        # position을 뒤로가면서 초기화
        while room_full[pos_assigned + 1]:
            pos_assigned += 1
        for index in range(pos_assigned, -1, -1):
            if not room_full[index]:
                break
            room_move_pos[index] = pos_assigned + 1
    return assign_room


k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution2(k, room_number))