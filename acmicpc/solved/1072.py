X, Y = map(int, input().split())

pre_percent = int(100 * Y / X)
if pre_percent >= 99:
    print(-1)
else:
    from math import ceil
    result = ceil((100 * Y - (pre_percent + 1) * X) / (pre_percent - 99))
    print(result)
