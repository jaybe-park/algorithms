import sys
sys.setrecursionlimit(40000)

dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

N = int(input())
bamboos = []
for __ in range(N):
    bamboos.append(list(map(int, input().split())))

cache = [[-1] * N for __ in range(N)]

def find_ans(bamboos, cache, target_inx, target_jnx):
    # Cache Check
    if cache[target_inx][target_jnx] != -1:
        return cache[target_inx][target_jnx]
    
    next_result = 0
    for d in dirs:
        curr_inx, curr_jnx = target_inx + d[0], target_jnx + d[1]
        if curr_inx >= N or curr_inx < 0:
            continue
        if curr_jnx >= N or curr_jnx < 0:
            continue

        if bamboos[target_inx][target_jnx] < bamboos[curr_inx][curr_jnx]:        
            next_result = max(next_result, find_ans(bamboos, cache, target_inx + d[0], target_jnx + d[1]))
    
    cache[target_inx][target_jnx] = next_result + 1
    return next_result + 1

for inx in range(N):
    for jnx in range(N):
        if cache[inx][jnx] != -1:
            continue
        cache[inx][jnx] = find_ans(bamboos, cache, inx, jnx)

result = 0
for row in cache:
    result = max(result, *row)

print(result)