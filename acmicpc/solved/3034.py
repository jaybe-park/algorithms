import math
N, W, H = map(int, input().split())
matches = [int(input()) for inx in range(N)]

max_length = math.sqrt(W ** 2 + H ** 2)
for match in matches:
    if match > max_length:
        print('NE')
    else:
        print('DA')
