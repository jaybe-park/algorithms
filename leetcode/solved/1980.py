from itertools import product

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        total = set(map(lambda x: ''.join(x), product(['0', '1'], repeat=len(nums))))
        results = list(total - set(nums))
        return results[0]