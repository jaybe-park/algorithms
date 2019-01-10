E, F, C = map(int, input().split())

curr_bottle = E + F
result = 0
while curr_bottle >= C:
    curr_exchange = int(curr_bottle / C)
    result = result + curr_exchange
    curr_bottle = curr_bottle % C + curr_exchange
print(result)