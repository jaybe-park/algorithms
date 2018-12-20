N = int(input())
nums = []
for __ in range(N):
    nums.append(int(input()))


nums.sort()

# mean
from statistics import mean
print(round(mean(nums)))

# median
print(nums[len(nums) // 2])

# mode
from collections import Counter
ctr = Counter(nums)
m_c = ctr.most_common()

mode_candidate = []
for m in m_c:
    if m[1] == m_c[0][1]:
        mode_candidate.append(m[0])
    else:
        break

if len(mode_candidate) > 1:
    mode_candidate.sort()
    print(mode_candidate[1])
else:
    print(mode_candidate[0])



# range
print(nums[len(nums) - 1] - nums[0])



