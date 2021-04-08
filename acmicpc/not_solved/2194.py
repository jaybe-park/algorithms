N, M, A, B, K = map(int, input().split())
obstacles = [tuple(map(lambda x: int(x) - 1, input().split())) for __ in range(K)]
start_point = tuple(map(lambda x: int(x) - 1, input().split()))
end_point = tuple(map(lambda x: int(x) - 1, input().split()))

def is_inbound(x, y):
    if x < 0 or y < 0 or x > N - A or y > M - B:
        return False
    return True

is_movable = [[True] * M for __ in range(N)]
for x, y in obstacles:
    is_movable[x][y] = False
    
    for inx in range(A):
        curr_x = x - inx
        for jnx in range(B):
            curr_y = y - jnx
            if is_inbound(curr_x, curr_y):
                is_movable[curr_x][curr_y] = False
            else:
                break
    
directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

cache = [[-1] * M for __ in range(N)]

# start_point setting
q = [(start_point, 0)]

def expand(curr_point, curr_dist):
    curr_x, curr_y = curr_point

    for x_dir, y_dir in directions:
        next_x, next_y = curr_x + x_dir, curr_y + y_dir
        if is_inbound(next_x, next_y) and is_movable[next_x][next_y]:
            next_dist = curr_dist + 1

            if cache[next_x][next_y] == -1 or cache[next_x][next_y] > next_dist:
                q.append(((next_x, next_y), next_dist))

def print_2d(arr):
    for row in arr:
        print(*row)

print_2d(is_movable)


while len(q) != 0:
    print(q)
    print_2d(cache)
    curr_point, curr_dist = q.pop(0)
    (curr_x, curr_y) = curr_point

    # 0. destination check
    if curr_point == end_point:
        if cache[curr_x][curr_y] == -1 or cache[curr_x][curr_y] > curr_dist:
            cache[curr_x][curr_y] = curr_dist
        continue

    # 1. visit check
    if cache[curr_x][curr_y] != -1 and cache[curr_x][curr_y] <= curr_dist:
        continue

    # 2. visit
    cache[curr_x][curr_y] = curr_dist

    # 3. expand
    expand(curr_point, curr_dist)
    pass

print_2d(cache)
print(cache[end_point[0]][end_point[1]])


