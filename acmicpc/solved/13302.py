N, M = map(int, input().split())
if M == 0:
    cant_go = []
else:
    cant_go = list(map(int, input().split()))

if N == M:
    print(0)
else:
    calender = [True] * N
    for day in cant_go:
        calender[day - 1] = False

    cache = [[-1] * (N + 1) for inx in range(N + 1)]

    def go_resort(curr_day, coupon_count):
        if curr_day >= N:
            return 0
            
        if cache[coupon_count][curr_day] != -1:
            return cache[coupon_count][curr_day]

        if not calender[curr_day]:
            cache[coupon_count][curr_day] = go_resort(curr_day + 1, coupon_count)
            return cache[coupon_count][curr_day]

        curr_money = 100 * 10000
        if coupon_count >= 3:
            curr_money = min(curr_money, go_resort(curr_day + 1, coupon_count - 3))
        
        curr_money = min(curr_money, 10000 + go_resort(curr_day + 1, coupon_count))
        curr_money = min(curr_money, 25000 + go_resort(curr_day + 3, coupon_count + 1))
        curr_money = min(curr_money, 37000 + go_resort(curr_day + 5, coupon_count + 2))
        
        cache[coupon_count][curr_day] = curr_money

        return curr_money

    print(go_resort(0, 0))
