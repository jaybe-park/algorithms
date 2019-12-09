from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        before_group = defaultdict(list)
        result = list()
        for inx, group_len in enumerate(groupSizes):
            before_group[group_len].append(inx)
            if group_len == len(before_group[group_len]):
                result.append(before_group[group_len])
                before_group[group_len] = list()
        
        return result