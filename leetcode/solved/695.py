class Solution:
    def is_in(self, x, y, m, n):
        if x < 0 or y < 0:
            return False
        if x >= m or y >= n:
            return False
        return True

    def is_visited(self, x, y, cache):
        if cache[x][y] == 0:
            return True
        else:
            return False

    def spread(self, cache, x, y, m, n, area):
        # boundary check
        if not self.is_in(x, y, m, n):
            return 0
        # visit check
        if self.is_visited(x, y, cache):
            return 0

        # visit
        cache[x][y] = 0

        curr_area = area + 1

        curr_area = max(curr_area, self.spread(cache, x - 1, y, m, n, curr_area))
        curr_area = max(curr_area, self.spread(cache, x + 1, y, m, n, curr_area))
        curr_area = max(curr_area, self.spread(cache, x, y - 1, m, n, curr_area))
        curr_area = max(curr_area, self.spread(cache, x, y + 1, m, n, curr_area))
        
        return curr_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = deepcopy(grid)
        
        result = 0
        for x in range(m):
            for y in range(n):
                if cache[x][y] == 1:
                    curr_spread = self.spread(cache, x, y, m, n, 0)
                    result = max(result, curr_spread)
        
        return result