T = int(input())

for __ in range(T):
    N = int(input())
    clothes = dict()
    for ___ in range(N):
        name, category = input().split()
        try:
            clothes[category] += 1
        except KeyError as KE:
            clothes[category] = 1
    
    result = 1
    for key in clothes.keys():
        result = result * (clothes[key] + 1)
    print(result - 1)