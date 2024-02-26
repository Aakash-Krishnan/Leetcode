class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Cols = len(heights), len(heights[0])
        pac, alt = set(), set()
        
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or not(0 <= r < Rows) or not(0 <= c< Cols) or heights[r][c] < prevHeight:
                return 
            
            visit.add((r, c))
            for dx, dy in dirx:
                dx += r
                dy += c
                dfs(dx, dy, visit, heights[r][c])
        
        for c in range(Cols):
            dfs(0, c , pac, heights[0][c])
            dfs(Rows - 1, c, alt, heights[Rows-1][c])
        
        for r in range(Rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, Cols-1, alt, heights[r][Cols-1])
        
        res = []
        for r in range(Rows):
            for c in range(Cols):
                if (r, c) in pac and (r, c) in alt:
                    res.append((r, c))
        
        return res