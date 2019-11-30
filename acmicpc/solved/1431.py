import sys
N = int(sys.stdin.readline())
target = []
for __ in range(N):
    target.append(sys.stdin.readline().rstrip())

def get_number_sum(target_str):
    result = 0
    for c in target_str:
        if c.isdigit():
            result += int(c)
    return result

target.sort()
target.sort(key=lambda x: get_number_sum(x))
target.sort(key=lambda x: len(x))

for s in target:
    print(s)
