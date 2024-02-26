class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[0] * m for _ in range(n)]
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < n) or not(0 <= c < m) or visited[r][c] or board[r][c] != word[i]:
                return False
            
            visited[r][c] = 1
            
            for dx, dy in dirx:
                if dfs(dx + r, dy + c, i+1):
                    visited[r][c] = 0
                    return True
            
            visited[r][c] = 0
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0): return True
        
        return False