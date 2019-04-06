import sys

def solve(triangle, cache, inx, jnx):
    N = len(triangle)
    
    if inx == N - 1:
        return triangle[inx][jnx]

    if cache[inx][jnx] == -1:
        cache[inx][jnx] = triangle[inx][jnx] + max(solve(triangle, cache, inx + 1, jnx), solve(triangle, cache, inx + 1, jnx + 1))
    
    return cache[inx][jnx]

C = int(sys.stdin.readline())
for ___ in range(C):
    N = int(sys.stdin.readline())
    triangle = []
    cache = []
    for inx in range(N):
        triangle.append(list(map(int, sys.stdin.readline().split())))
        cache.append([-1] * (inx + 1))

    print(solve(triangle, cache, 0, 0))
    
    
    