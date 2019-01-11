A, B = input().split()

target_c = ''
for c in A:
    if c in B:
        target_c = c
        break
A_index = A.index(target_c)
B_index = B.index(target_c)

result = [['.'] * len(A) for __ in range(len(B))]

for inx in range(len(A)):
    result[B_index][inx] = A[inx]
for inx in range(len(B)):
    result[inx][A_index] = B[inx]

for row in result:
    print(''.join(row))