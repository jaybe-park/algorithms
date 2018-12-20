nums = list(range(1, int(input()) + 1))
while len(nums) != 1:
    inx = 0
    while inx < len(nums):
        del nums[inx]
        inx = inx + 1
print(nums[0])

# list 직접 삭제는 시간이 너무 많이 걸림
# 조세퍼스 문제 같은데 python은 어떻게 풀어야 할까