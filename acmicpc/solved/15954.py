from decimal import Decimal

N, K = map(int, input().split())
nums = list(map(int, input().split()))
square_nums = list(map(lambda x: x ** 2, nums))

result = Decimal('INF')
for inx in range(N - K + 1):
    initial_sum = sum(nums[inx : inx + K])
    initial_squere_sum = sum(square_nums[inx : inx + K])
    result = min(result, (Decimal(initial_squere_sum) / K - (Decimal(initial_sum) / K) ** 2).sqrt())
    for jnx in range(inx + K, N):
        initial_sum += nums[jnx]
        initial_squere_sum += square_nums[jnx]
        result = min(result, (Decimal(initial_squere_sum) / (jnx + 1 - inx) - (Decimal(initial_sum) / (jnx + 1 - inx)) ** 2).sqrt())

print(result)
