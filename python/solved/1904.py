N = int(input())

def find_ans(cache, target_num):
    if cache[target_num] != -1:
        return cache[target_num]
    

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    cache = [-1] * (N + 1)
    cache[1] = 1
    cache[2] = 2
    curr_sum = 3
    for inx in range(3, N + 1):
        cache[inx] = curr_sum % 15746
        curr_sum = (curr_sum - cache[inx - 2] + cache[inx]) % 15746

    print(cache[N])