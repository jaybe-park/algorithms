N = int(input())
nums = list(map(int, input().split()))

max_val = [nums[0]]
for inx, num in enumerate(nums[1:]):
    max_val.append(max(num, num + max_val[inx]))

print(max(max_val))