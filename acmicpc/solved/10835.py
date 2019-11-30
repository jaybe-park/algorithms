N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum(filter(lambda x : x < max(a), b)))