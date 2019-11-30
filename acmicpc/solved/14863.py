import sys

N, K = map(int, sys.stdin.readline().split())

# First
pre_d = dict()
walk_time, walk_money, bike_time, bike_money = map(int, sys.stdin.readline().split())
pre_d[walk_time] = walk_money
if bike_time in pre_d:
    pre_d[bike_time] = max(pre_d[bike_time], bike_money)
else:
    pre_d[bike_time] = bike_money

for __ in range(N - 1):
    d = dict()
    walk_time, walk_money, bike_time, bike_money = map(int, sys.stdin.readline().split())

    for k in pre_d.keys():
        if k + walk_time <= K:
            if k + walk_time in d:
                d[k + walk_time] = max(d[k + walk_time], pre_d[k] + walk_money)
            else:
                d[k + walk_time] = pre_d[k] + walk_money
        
        if k + bike_time <= K:
            if k + bike_time in d:
                d[k + bike_time] = max(d[k + bike_time], pre_d[k] + bike_money)
            else:
                d[k + bike_time] = pre_d[k] + bike_money
    pre_d = d

print(max(pre_d.values()))
