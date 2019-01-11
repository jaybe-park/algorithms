N, T = map(int, input().split())
tasks = list(map(int, input().split()))

curr_time = 0
result = -1
for inx, task in enumerate(tasks):
    curr_time += task
    if T < curr_time:
        result = inx
        break

if result == -1:
    result = N

print(result)
