class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for inx in range(len(nums)):
            for jnx in range(inx + 1, len(nums)):
                if nums[inx] + nums[jnx] == target:
                    return [inx, jnx]