# Solving Date: 20.03.28.


def grab_item(board, move):
    item = None
    for line in board:
        if line[move] != 0:
            item = line[move]
            line[move] = 0
            break
    return item


def solution(board, moves):
    basket = []
    pop_count = 0
    for move in moves:
        move -= 1
        item = grab_item(board, move)
        if item is not None:
            basket.append(item)
            while len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                pop_count += 2
    return pop_count
