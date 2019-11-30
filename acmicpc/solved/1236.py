N, M = map(int, input().split())
garo = set()
sero = set()
for inx in range(N):
    input_str = input()
    for jnx in range(len(input_str)):
        if input_str[jnx] == 'X':
            garo.add(inx + 1)
            sero.add(jnx + 1)

print(max(N - len(garo), M - len(sero)))