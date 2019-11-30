import math

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums_squared = list(map(lambda x : x ** 2, nums))

result = -1

for inx in range(0, N - K):
    target_slice = slice(inx, inx + K)
    squared_avg = sum(nums_squared[target_slice]) / float(len(nums_squared[target_slice]))
    avg_square = (sum(nums[target_slice]) / float(len(nums[target_slice]))) ** 2

    result = max(result, squared_avg - avg_square)

print(math.sqrt(result))