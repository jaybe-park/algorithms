C = int(input())

ns = []
ms = []
for __ in range(C):
    n, m = map(int, input().split())
    ns.append(n)
    ms.append(m)

states = []
states.append({0: 1})

for inx in range(max(ms)):
    curr_state = states[-1]
    next_state = dict()

    for h, p in curr_state.items():
        try:
            next_state[h + 2] += p * 0.75
        except KeyError as KE:
            next_state[h + 2] = p * 0.75

        try:
            next_state[h + 1] += p * 0.25
        except KeyError as KE:
            next_state[h + 1] = p * 0.25
    states.append(next_state)

for inx in range(C):
    curr_n = ns[inx]
    curr_m = ms[inx]

    result = 0
    curr_state = states[curr_m]
    for h in filter(lambda x: x >= curr_n, curr_state.keys()):
        result += curr_state[h]
    print(result)