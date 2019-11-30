from collections import deque


N, K = map(int, input().split())
q = deque()
cache = [-1] * 200000

def find(x, v):
    if x < 0 or x > 100005:
        return
    if cache[x] != -1 and cache[x] <= v:
        return
    
    
    cache[x] = v
    q.append([x - 1, v + 1])
    q.append([x + 1, v + 1])
    q.append([2 * x, v + 1])

q.append([N, 0])

while len(q) != 0:
    x, v = q.popleft()
    find(x, v)

print(str(cache[K]))