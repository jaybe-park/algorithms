from math import gcd

A, B = map(int, input().split())
print(gcd(int('1' * A), int('1' * B)))

# 메모리 초과