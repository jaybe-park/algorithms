N, M = map(int, input().split())
cache = [False] * (N + 1)

ks = list(map(int, input().split()))
for k in ks:
    for inx in range(k, N + 1, k):
        cache[inx] = True

result = 0
for inx in range(len(cache)):
    if cache[inx]:
        result += inx
print(result)