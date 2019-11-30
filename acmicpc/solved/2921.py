N = int(input())
result = 0

for inx in range(0, N + 1):
    for jnx in range(inx, N + 1):
        result = result + inx + jnx

print(result)