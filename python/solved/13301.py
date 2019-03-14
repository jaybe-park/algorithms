N = int(input())
if N == 1:
    print(4)
else:
    fivo = [1, 1]
    while len(fivo) < N:
        fivo.append(fivo[-1] + fivo[-2])

    print(4 * fivo[-1] + 2 * fivo[-2])