class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        Col = len(grid[0])
        col = 0
        for row in range(len(grid)-1, -1, -1):
            while col < Col and grid[row][col] >= 0:
                col += 1
            res += len(grid[0]) - col
        
        return res
