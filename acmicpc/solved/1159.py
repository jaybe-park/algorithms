N = int(input())

name_count = dict()

for __ in range(N):
    name = input()
    try:
        name_count[name[0]] = name_count[name[0]] + 1
    except Exception as E:
        name_count[name[0]] = 1

result = []
for k in sorted(name_count.keys()):
    if name_count[k] >= 5:
        result.append(k)

if len(result) == 0:
    print('PREDAJA')
else:
    print(''.join(result))