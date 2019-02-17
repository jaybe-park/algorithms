N = int(input())
M = int(input())
nums = list(map(int, input().split()))
check = [False] * 100001

result = 0
for num in nums:
    if M - num <= 100000 and M - num >= 0 and check[M - num]:
        result += 1
    check[num] = True
print(result)