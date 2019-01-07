N = int(input())
nums = list(map(int, input().split()))
result = []
result.append(nums[0])
for inx in range(1, N):
    if nums[inx] == 0:
        result.append(0)
    else:
        result.append(result[inx - 1] + 1)

print(sum(result))
