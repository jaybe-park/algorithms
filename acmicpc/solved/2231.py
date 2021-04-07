N = int(input())

n = N
result = 0
while n > 0:
    n -= 1
    if n + sum(map(int, list(str(n)))) == N:
        result = n

print(result)