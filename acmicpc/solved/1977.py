M = int(input())
N = int(input())

import math
min = math.ceil(math.sqrt(M))

if min ** 2 > N:
    print(-1)
else:
    max = math.floor(math.sqrt(N))
    nums = []
    for inx in range(min, max + 1):
        nums.append(inx ** 2)
    
    print(sum(nums))
    print(nums[0])