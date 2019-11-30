class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for inx in range(len(points) - 1):
            result += max(abs(points[inx][0] - points[inx + 1][0]), abs(points[inx][1] - points[inx + 1][1]))
        return result