N, J = map(int, input().split())
heights = list(map(int, input().split()))

for __ in range(J):
    start, direction, count = input().split()
    start, count = map(int, (start, count))

    if direction == 'L':
        target = heights[start - count - 1:start - 1]
    else:
        target = heights[start: start + count]
    # print(target)
    print(max(target))

    if direction == 'L':
        heights.insert(start - count, heights.pop(start - 1))
    else:
        heights.insert(start + count, heights.pop(start - 1))
    # print(heights)
