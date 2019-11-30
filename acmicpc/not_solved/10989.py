T = int(input())

for __ in range(T):
    N, M = map(int, input().split())
    for ___ in range(N):
        curr = input()
        print(curr[::-1])