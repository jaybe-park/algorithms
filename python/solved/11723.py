import sys

S = [False] * 20
all = [True] * 20
empty = [False] * 20
N = int(sys.stdin.readline())
for __ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        S[int(command[1]) - 1] = True
    if command[0] == 'remove':
        S[int(command[1]) - 1] = False
    if command[0] == 'check':
        if S[int(command[1]) - 1]:
            print(1)
        else:
            print(0)
    if command[0] == 'toggle':
        S[int(command[1]) - 1] = not S[int(command[1]) - 1]
    if command[0] == 'all':
        S = all
    if command[0] == 'empty':
        S = empty