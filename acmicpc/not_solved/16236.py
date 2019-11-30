import sys
input = sys.stdin.readline

N = int(input())
space = []

class Shark():
    def __init__(self):
        self.length = 2
        self.eated = 0
        self.x = 0
        self.y = 0

shark = Shark()

for inx in range(N):
    space.append(list(map(int, input().split())))
    if 9 in space[-1]:
        shark.x = inx
        shark.y = space[-1].index(9)
        space[shark.x][shark.y] = 0

def is_in_space(inx, jnx):
    if inx < 0 or inx >= N or jnx < 0 or jnx >= N:
        return False
    else:
        return True

def explore(space, visited, eatable, inx, jnx, shark):
    # Condition Check
    if not is_in_space(inx, jnx):
        return

    # Visited Check
    if visited[inx][jnx]:
        return
    visited[inx][jnx] = True

    # Length Check
    if space[inx][jnx] != 0:
        if space[inx][jnx] < shark.length:
            eatable.append((abs(shark.x - inx) + abs(shark.y - jnx), inx, jnx))
        elif space[inx][jnx] > shark.length:
            return

    explore(space, visited, eatable, inx, jnx + 1, shark)      # North
    explore(space, visited, eatable, inx, jnx - 1, shark)      # South
    explore(space, visited, eatable, inx + 1, jnx, shark)      # East
    explore(space, visited, eatable, inx - 1, jnx, shark)      # West
    
time = 0
while True:
    eatable = []
    visited = [[False] * N for __ in range(N)]

    explore(space, visited, eatable, shark.x, shark.y + 1, shark)      # North
    explore(space, visited, eatable, shark.x, shark.y - 1, shark)      # South
    explore(space, visited, eatable, shark.x + 1, shark.y, shark)      # East
    explore(space, visited, eatable, shark.x - 1, shark.y, shark)      # West
    
    
    if len(eatable) == 0:
        break

    min_dist = min(map(lambda x: x[0], eatable))
    eatable = list(filter(lambda x: x[0] == min_dist, eatable))
    eatable.sort(key=lambda x: x[2])
    eatable.sort(key=lambda x: x[1])
    print(eatable)
    time += eatable[0][0]

    # Eat
    shark.x = eatable[0][1]
    shark.y = eatable[0][2]
    space[shark.x][shark.y] = 0
    shark.eated += 1
    if shark.length == shark.eated:
        shark.length += 1
        shark.eated = 0

print(time)


