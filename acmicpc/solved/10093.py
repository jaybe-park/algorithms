l, r = sorted(list(map(int, input().split())))
if l == r:
    print(0)
else:
    print(r - l - 1)
print(' '.join(map(str, range(l + 1, r))))