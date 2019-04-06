import sys

def solve(board, cache, inx, jnx):
    N = len(board)
    if inx < 0 or inx >= N or jnx < 0 or jnx >= N:
        return False
    
    if cache[inx][jnx] != -1:
        return cache[inx][jnx]

    if inx == jnx == N - 1:
        return True

    cache[inx][jnx] = any([solve(board, cache, inx + board[inx][jnx], jnx), solve(board, cache, inx, jnx + board[inx][jnx])])

    return cache[inx][jnx]
 



C = int(sys.stdin.readline())
for ___ in range(C):
    N = int(sys.stdin.readline())
    board = []
    for __ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    cache = [[-1] * N for ____ in range(N)]
    if solve(board, cache, 0, 0):
        print('YES')
    else:
        print('NO')
