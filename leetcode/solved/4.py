from collections import deque
from math import floor

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 0:
            is_even = True
        else:
            is_even = False
        
        target_inx = floor((m + n) / 2)
        print(target_inx)
        sorted_nums = deque()

        while len(sorted_nums) <= target_inx:
            if len(nums1) == 0:
                sorted_nums.append(nums2.pop(0))
            elif len(nums2) == 0:
                sorted_nums.append(nums1.pop(0))
            elif nums1[0] > nums2[0]:
                sorted_nums.append(nums2.pop(0))
            else:
                sorted_nums.append(nums1.pop(0))

        print(sorted_nums)

        if is_even:
            return (sorted_nums[-1] + sorted_nums[-2]) / 2
        else:
            return sorted_nums[-1]
