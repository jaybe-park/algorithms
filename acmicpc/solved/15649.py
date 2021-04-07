from itertools import permutations

N, M = map(int, input().split())

p = permutations(range(1, N + 1), M)
for d in p:
    print(*d)

