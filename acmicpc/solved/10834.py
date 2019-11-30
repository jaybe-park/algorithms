M = int(input())
result = 1
result_dir = 0
for __ in range(M):
    pre, post, dir = map(int, input().split())
    result_dir += dir
    result = result * post / pre
print('%d %d' % (result_dir % 2, int(result)))