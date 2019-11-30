while True:
    nums = sorted(list(map(int, input().split())))

    if nums[0] == nums[1] == nums[2] == 0:
        break
    
    if (nums[0] * nums[0] + nums[1] * nums[1]) == nums[2] * nums[2]:
        print('right')
    else:
        print('wrong')