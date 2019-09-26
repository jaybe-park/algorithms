buttons = list(map(int, input().split()))
result = 5000 - 500 * buttons.count(1) - 800 * buttons.count(2) - 1000 * buttons.count(3)
print(result)