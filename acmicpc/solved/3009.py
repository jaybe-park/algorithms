xs, ys = [], []
for __ in range(3):
    curr_x, curr_y = map(int, input().split())
    xs.append(curr_x)
    ys.append(curr_y)
result = []
for x in xs:
    if xs.count(x) == 1:
        result.append(x)

for y in ys:
    if ys.count(y) == 1:
        result.append(y)

print(' '.join(map(str, result)))