class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rotated = list(zip(*grid))
        
        row_max = list(map(max, grid))
        col_max = list(map(max, rotated))

        increased = []
        for inx in range(N):
            curr_row = []
            for jnx in range(N):
                curr_row.append(min(row_max[inx], col_max[jnx]))
            increased.append(curr_row)

        return sum(map(sum, increased)) - sum(map(sum, grid))
        