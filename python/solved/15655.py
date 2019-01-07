from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = []
combi_result = combinations(nums, M)
for curr_result in combi_result:
    result.append(list(sorted(curr_result)))

result.sort()

for curr_result in result:
    print(' '.join(map(str, curr_result)))