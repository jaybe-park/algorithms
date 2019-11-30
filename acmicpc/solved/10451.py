import sys
sys.setrecursionlimit(2000)

T = int(input())

def find_cycle(nums, check, curr_num):
    if check[curr_num]:
        return

    check[curr_num] = True
    find_cycle(nums, check, nums[curr_num])

result_nums = []
for __ in range(T):
    N = int(input())
    nums = list(map(lambda x : int(x) - 1, input().split()))
    check = [False] * N
    result = 0
    for inx in range(N):
        if not check[inx]:
            result = result + 1
            find_cycle(nums, check, inx)

    result_nums.append(result)

print('\n'.join(map(str, result_nums)))    