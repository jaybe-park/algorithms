N = int(input())
lower = 2
for __ in range(N):
    lower = lower * 2 - 1
print(lower ** 2)