# 시간 초과


NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

def dig(x):
    while x >= 10:
        x = sum(map(int, str(x)))
    return x

def go(distance, direction, position):
    if direction == NORTH:
        position[1] = position[1] + distance
    elif direction == EAST:
        position[0] = position[0] + distance
    elif direction == SOUTH:
        position[1] = position[1] - distance
    else:
        position[0] = position[0] - distance


T = int(input())
for _ in range(T):
    position = [0, 0]
    direction = NORTH
    gold_number = 1

    K, M = map(int, input().split())

    for __ in range(K):
        distance = dig(gold_number)
        go(distance, direction, position)
        direction = (direction + 1) % 4
        gold_number = gold_number * M

    print(' '.join(map(str, position)))
