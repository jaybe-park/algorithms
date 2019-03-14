from math import ceil
N, K = map(int, input().split())
check_list = [[0] * 2 for __ in range(6)]
for __ in range(N):
    sex, year = map(int, input().split())
    check_list[year - 1][sex] += 1
result = 0
for m, f in check_list:
    result += ceil(m / K)
    result += ceil(f / K)
print(result)