N = int(input())
result = 0
for __ in range(N):
    s, a = map(int, input().split())
    result += a % s
print(result)