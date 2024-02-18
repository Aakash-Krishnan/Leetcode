class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        N, M = len(A), len(A[0])
        Islands = 0
        visited = [[0] * M for _ in range(N)]
        dirx = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        def dfs(i, j):
            visited[i][j] = 1
            for dx, dy in dirx:
                dx = i + dx
                dy = j + dy
                if check(dx, dy):
                    dfs(dx, dy)
        
        def check(I, J):
            if (0 <= I < N) and (0 <= J < M) and A[I][J] == "1" and not visited[I][J]:
                return True
            return False 

        for i in range(N):
            for j in range(M):
                if A[i][j] == "1" and not visited[i][j]:
                    Islands += 1
                    dfs(i, j)
                    
        return Islands