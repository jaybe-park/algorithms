import sys

N, M = map(int, sys.stdin.readline().split())
result = list(range(1, N + 1))

for __ in range(M):
    k, v = map(int, sys.stdin.readline().split())
    result[k - 1] += 1
    result[v - 1] -= 1

from collections import Counter

if Counter(result).most_common(1)[0][1] == 1:
    print(*result)
else:
    print(str(-1))