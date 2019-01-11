def rotate(original):
    return list(map(lambda x: list(x), zip(*reversed(original))))

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate(original)

for row in original:
    print(*row)
for row in rotated:
    print(*row)