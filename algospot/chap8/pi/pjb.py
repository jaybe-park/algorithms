# Python으로는 안풀리는 듯
# https://algospot.com/forum/read/3092/

import sys
sys.setrecursionlimit(1000000)
INF = 1234567890

def is_identical(target):
    return target.count(target[0]) == len(target)

def is_incre_decre_by_one(target):
    joined = ''.join(map(str, target))

    return joined in '0123456789' or joined in '9876543210'

def is_dc(target):
    if target[1] - target[0] == 0:
        return False

    if target[0] < target[-1]:
        dc = list(range(target[0], target[-1] + 1, target[1] - target[0]))
    else:
        dc = list(range(target[0], target[-1] - 1, target[1] - target[0]))

    return target == dc

def is_two_num(target):
    even_slice, odd_slice = slice(0, len(target) + 1, 2), slice(1, len(target) + 1, 2)
    return is_identical(target[even_slice]) and is_identical(target[odd_slice])

def get_score(target):
    if is_identical(target):
        return 1
    elif is_incre_decre_by_one(target):
        return 2
    elif is_two_num(target):
        return 4
    elif is_dc(target):
        return 5
    else:
        return 10



def solve(nums, cache):
    N = len(nums)
    cache_idx = len(cache) - N

    if N == 0:
        return 0

    if cache[cache_idx] != -1:
        return cache[cache_idx]

    result = INF

    if N >= 3:
        result = min(result, get_score(nums[:3]) + solve(nums[3:], cache))
    if N >= 4:
        result = min(result, get_score(nums[:4]) + solve(nums[4:], cache))
    if N >= 5:
        result = min(result, get_score(nums[:5]) + solve(nums[5:], cache))

    cache[cache_idx] = result

    return result    

C = int(sys.stdin.readline())
for __ in range(C):
    nums = list(map(int, sys.stdin.readline().strip()))
    cache = [-1] * len(nums)
    cache[-1] = INF
    cache[-2] = INF

    print(solve(nums, cache))
