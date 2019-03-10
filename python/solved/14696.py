import sys
N = int(sys.stdin.readline())
data = slice(1, 200)

def guess_who_wins(A, B):
    if A.count(4) > B.count(4):
        return 1
    if A.count(4) < B.count(4):
        return -1
    if A.count(3) > B.count(3):
        return 1
    if A.count(3) < B.count(3):
        return -1
    if A.count(2) > B.count(2):
        return 1
    if A.count(2) < B.count(2):
        return -1
    if A.count(1) > B.count(1):
        return 1
    if A.count(1) < B.count(1):
        return -1
    return 0

for __ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    winner = guess_who_wins(A[data], B[data])
    if winner == 1:
        print('A')
    elif winner == -1:
        print('B')
    else:
        print('D')
    