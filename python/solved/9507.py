T = int(input())
nums = []
for __ in range(T):
    nums.append(int(input()))

def find_fivo():
    fivo = [1, 1, 2, 4, 8]
    fivo_sum = [1, 2, 4, 8, 16]

    for inx in range(5, 68):
        fivo.append(fivo_sum[inx - 1] - fivo_sum[inx - 5])
        fivo_sum.append(fivo[inx] + fivo_sum[inx - 1])

    return fivo

fivo = find_fivo()
for inx in nums:
    print(fivo[inx])