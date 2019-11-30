A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
Y = 0
if C >= P:
    Y = B
else:
    Y = B + D * (P - C)

print(min(X, Y))