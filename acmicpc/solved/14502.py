from itertools import combinations
from copy import deepcopy

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N, M = map(int, input().split())
room = []
for __ in range(N):
    room.append(list(map(int, input().split())))
initial_room = deepcopy(room)

def select_3_xy(N, M):
    xys = []
    for x in range(N):
        for y in range(M):
            xys.append((x, y))

    list(combinations(xys, 3))

    return list(combinations(xys, 3))

xys = select_3_xy(N, M)

def spread_virus(room, xy):
    x, y = xy

    if x < 0 or x >= N:
        return
    elif y < 0 or y >= M:
        return

    if room[x][y] == 0:
        room[x][y] = 2
        for dir_x, dir_y in DIR:
            spread_virus(room, (x + dir_x, y + dir_y))
    else:
        return

def get_safety_zone(room):
    result = 0
    
    for row in room:
        result += row.count(0)

    return result

safety_zone = 0

for xy in xys:
    room = deepcopy(initial_room)

    pre_pixels = []
    for x, y in xy:
        pre_pixels.append(room[x][y])

    if set(pre_pixels) == {0}:
        for x, y in xy:
            room[x][y] = 1

        initial_virus = []
        for x in range(N):
            for y in range(M):
                if room[x][y] == 2:
                    initial_virus.append((x, y))

        for virus_x, virus_y in initial_virus:
            for dir_x, dir_y in DIR:
                spread_virus(room, (virus_x + dir_x, virus_y + dir_y))

        curr_safety_zone = get_safety_zone(room)
        if safety_zone < curr_safety_zone:
            safety_zone = curr_safety_zone
print(safety_zone)