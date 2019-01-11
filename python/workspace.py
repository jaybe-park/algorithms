N, C = map(int, input().split())
sky = [False] * (C + 1)

result = 0

for __ in range(N):
    period = int(input())
    for inx in range(period, len(sky), period):
        if not sky[inx]:
            sky[inx] = True
            result += 1


print(result)