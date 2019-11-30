from itertools import permutations
N = int(input())
perm = permutations(list(range(1, N + 1)))
for p in perm:
    print(*p)