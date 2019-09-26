T = int(input())

for __ in range(T):
    N = int(input())

    hakjum = 0
    sungjuk = 0.0
    for ___ in range(N):
        h_str, s_str = input().split()
        hakjum += int(h_str)
        sungjuk += float(h_str) * float(s_str)
    
    print(hakjum, sungjuk/hakjum)