cord = [-1, 0, 1]
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        cache = {}
        def dfs(r, c1, c2):
            global cord
            if c1 == c2 or (min(c1, c2) < 0) or max(c1, c2) == Cols:
                return 0
            if Rows - 1 == r:
                return grid[r][c1] + grid[r][c2]
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            
            res = 0
            
            for i in cord:
                for j in cord:
                    res = max(res, dfs(r+1, c1 + i, c2 + j))
                
            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]
            return cache[(r, c1, c2)]
        
        return dfs(0, 0, Cols-1)