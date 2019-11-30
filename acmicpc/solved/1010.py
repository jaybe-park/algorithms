import sys
T = int(sys.stdin.readline())
def solve(cache, left_site, right_site):
    if cache[left_site][right_site] != -1:
        return cache[left_site][right_site]

    remained_bridge = len(cache) - left_site - 1
    remained_site = len(cache[0]) - right_site - 1
    
    # Unable to build bridges
    if remained_bridge > remained_site:
        cache[left_site][right_site] = 0
        return cache[left_site][right_site]

    # Last left site
    if left_site == len(cache) - 1:
        cache[left_site][right_site] = 1
        return cache[left_site][right_site]

    result = 0
    for inx in range(right_site + 1, len(cache[0])):
        result += solve(cache, left_site + 1, inx)
    
    cache[left_site][right_site] = result
    return cache[left_site][right_site]

for __ in range(T):
    left, right = map(int, sys.stdin.readline().split())
    
    cache = [[-1] * right for ___ in range(left)]
    result = 0
    for inx in range(right):
        result += solve(cache, 0, inx)
    print(result)