M, N = map(int, input().split())

net = [False, False, True, True] + [False, True] * (int((N - 5) / 2) + 2)

for inx in range(3, N + 1):
    if net[inx]:
        for jnx in range(inx * 2, N + 1, inx):
            if net[jnx]:
                net[jnx] = False

for inx in range(M, N + 1):
    if net[inx]:
        print(inx)