import sys

def solve(cache, nums, target):
    # 1. Check Conditions
    if target >= len(cache):
        return 0
    
    # 2. Check cache - Memoization
    if cache[target] != -1:
        return cache[target]

    # 3. Solve - Optimal Substructure
    result = 1
    for inx in range(target + 1, len(cache)):
        if nums[target] < nums[inx]:
            result = max(result, 1 + solve(cache, nums, inx))
    
    # 4. Save Result to cache
    cache[target] = result
    
    # 5. Return Result
    return result

C = int(sys.stdin.readline())

for __ in range(C):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    cache = [-1] * N

    for inx in range(N):
        solve(cache, nums, inx)

    print(max(cache))