N = int(input())

cache = [1] * (N + 1)
two = 2
while two <= N:
    for inx in range(two, N + 1, two):
        cache[inx] = cache[inx] + 1
    two = two * 2

# odd
result = int(N / 2)
# even
for inx in range(2, N + 1, 2):
    result = result + 2 ** (cache[inx] - 1)

print(result * 2)