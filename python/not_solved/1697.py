import sys
sys.setrecursionlimit(10000000)

N, K = map(int, input().split())

cache = [-1] * N

for inx in range(N, K + 1):
    cache.append(inx - N)

def find_path(cache, curr_point, curr_step):
    
    # Arrive at Target Point
    if curr_point == K:
        if cache[curr_point] > curr_step:
            cache[curr_point] = curr_step
        return

    # If no cache, make cache
    if curr_point >= len(cache):
        for __ in range(curr_point - len(cache) +1):
            cache.append(-1)

    # If not short path, return
    if cache[curr_point] != -1 and cache[curr_point] < curr_step:
        return
    
    cache[curr_point] = curr_step
    
    # *2
    if curr_point <= int(K / 2) + 2:
        find_path(cache, curr_point * 2, curr_step + 1)

    # +1
    if curr_point < K:
        find_path(cache, curr_point + 1, curr_step + 1)

    # -1
    if curr_point >= 3:
        find_path(cache, curr_point - 1, curr_step + 1)





find_path(cache, 5, 0)
print(cache[K])






# 시간초과