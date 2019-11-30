from itertools import permutations

N = int(input())
K, *num = map(int, input().split())

perm = list(permutations(range(1, N + 1)))

if K == 1:
    print(*perm[num[0] - 1])
else:
    print(perm.index(tuple(num)) + 1)