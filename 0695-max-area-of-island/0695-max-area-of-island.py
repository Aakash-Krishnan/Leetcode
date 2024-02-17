class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res, cnt = 0, 0
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(r, c):
            nonlocal res, cnt
            cnt += 1
            res = max(res, cnt)
            
            visited[r][c] = 1
            for dx, dy in dirx:
                dx = r + dx
                dy = c + dy
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] and not visited[dx][dy]:
                    dfs(dx, dy)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cnt = 0
                    dfs(i ,j)
        
        return res