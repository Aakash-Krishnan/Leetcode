class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visit = set()
        
        def check(r, c):
            return (0 <= r < N) and (0 <= c < M)
        
        def dfs(r, c):
            if not check(r, c) or (r,c) in visit or not grid[r][c]:
                return 
            
            visit.add((r, c))
            for dx, dy in dirx:
                dx += r
                dy += c
                dfs(dx, dy)
                
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dx, dy in dirx:
                        dx += r
                        dy += c
                        if not check(dx,dy) or (dx, dy) in visit:
                            continue
                        if grid[dx][dy]:
                            return res

                        visit.add((dx,dy))
                        q.append((dx, dy))
                res += 1
        
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()
                    