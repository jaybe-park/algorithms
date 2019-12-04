class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for row in A:
            result.append(list(map(lambda x: x * -1 + 1, reversed(row))))
        
        return result