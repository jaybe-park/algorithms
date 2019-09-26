import sys
input = sys.stdin.readline

N = int(input())
sangdams = []
for __ in range(N):
    sangdams.append(list(map(int, input().split())))

cache = [-1] * N

def solve(sangdams, cache, inx):
    if inx == N:
        return 0
    
    if inx > N:
        return -1234567890
    
    if cache[inx] != -1:
        return cache[inx]

    result = 0

    # now
    result = max(result, sangdams[inx][1] + solve(sangdams, cache, inx + sangdams[inx][0]))

    # not now
    result = max(result, solve(sangdams, cache, inx + 1))

    cache[inx] = result

    return result

print(solve(sangdams, cache, 0))

