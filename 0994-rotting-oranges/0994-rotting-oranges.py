class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        inf = float("inf")
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        time = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] in [0, 1]:
                    time[i][j] = inf
                else:
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()
            for dx, dy in dirx:
                dx = x + dx
                dy = y + dy
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1 and time[dx][dy] > 1 + time[x][y]:
                    time[dx][dy] = 1 + time[x][y]
                    q.append((dx, dy))
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, time[i][j])
        
        return res if res != inf else -1