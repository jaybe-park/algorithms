N = int(input())
nums = []
for __ in range(N):
    nums.append(int(input()))

from collections import Counter
ctr = Counter(nums)
most_common = ctr.most_common()
most_common.sort(key=lambda x : x[0])

for pair in most_common:
    print((str(pair[0]) + '\n') * pair[1], end='')