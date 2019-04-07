import sys
C = int(sys.stdin.readline())
targets = []
for __ in range(C):
    targets.append(int(sys.stdin.readline()))

max_target = max(targets)

cache = [-1] * (max_target + 1)
cache[1] = 1
cache[2] = 2

for inx in range(3, max_target + 1):
    cache[inx] = (cache[inx - 1] + cache[inx - 2]) % 1000000007

for target in targets:
    print(cache[target])