import sys
N = int(sys.stdin.readline())
from collections import Counter
result = 0

for __ in range(N):
    curr_input = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(curr_input)
    m_c = cnt.most_common()
    curr_result = 0
    if m_c[0][1] == 3:
        curr_result = 10000 + 1000 * m_c[0][0]
    elif m_c[0][1] == 2:
        curr_result = 1000 + 100 * m_c[0][0]
    else:
        curr_result = max(curr_input) * 100
    if curr_result > result:
        result = curr_result

print(result)
