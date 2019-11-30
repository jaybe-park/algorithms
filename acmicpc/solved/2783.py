X, Y = map(int, input().split())
result = 1000 * X / Y

N = int(input())
for __ in range(N):
    X, Y = map(int, input().split())
    result = min(result, 1000 * X / Y)
print(result)