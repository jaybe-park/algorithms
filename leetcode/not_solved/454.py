from collections import Counter

class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        caches = [dict(), dict(), dict()]
        result = 0

        for val, c in Counter(A).most_common():
            result += self.get_result(caches, val, B, C, D) * c
        
        return result
    
    def get_result(self, caches, curr_sum, *lists):
        # Check Cache
        try:
            return caches[-1 * len(lists)][curr_sum]
        except:
            pass

        
        
        if len(lists) == 1:
            caches[-1 * len(lists)][curr_sum] = lists[0].count(-1 * curr_sum)
        else:
            curr_list = lists[0]
            result = 0

            for val, c in Counter(curr_list).most_common():
                result += self.get_result(caches, curr_sum + val, *lists[1:]) * c
            
            caches[-1 * len(lists)][curr_sum] = result
        
        return caches[-1 * len(lists)][curr_sum]