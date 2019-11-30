E, S, M = map(int, input().split())

RANGE_E, RANGE_S, RANGE_M = 15, 28, 19
year = S
if E == RANGE_E:
    E = 0
if M == RANGE_M:
    M = 0
while True:
    if (year % RANGE_E) == E and (year % RANGE_M) == M:
        break
    else:
        year = year + RANGE_S
print(year)