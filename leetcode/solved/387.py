from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s).most_common()
        
        counter_map = dict()
        for c, occurance in counter:
            counter_map[c] = occurance
        
        # print(counter_map)
        
        for inx, c in enumerate(s):
            if counter_map[c] == 1:
                return inx
            
        return -1