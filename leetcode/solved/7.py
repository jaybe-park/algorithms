class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        result = int(''.join(str(abs(x))[::-1]))
        if is_negative:
            result = -1 * result
        
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0
        