H, W = map(int, input().split())

for __ in range(H):
    result = [-1] * W

    input_map = input()
    for inx in range(W):
        if input_map[inx] == 'c':
            for jnx in range(inx, W):
                if result[jnx] == -1:
                    result[jnx] = jnx - inx
                else:
                    result[jnx] = min(result[jnx], jnx - inx)
    print(*result)    
    