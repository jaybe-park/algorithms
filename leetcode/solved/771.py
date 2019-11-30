class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for c in J:
            result += S.count(c)
            
        return result
        