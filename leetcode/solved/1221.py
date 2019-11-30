class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = 0
        result = 0
        
        for c in s:
            if c == 'R':
                stack += 1
            else:
                stack -= 1
            
            if stack == 0:
                result += 1
                
        return result
        