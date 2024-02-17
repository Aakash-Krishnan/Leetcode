class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        oldColor = image[sr][sc]
        q = deque()
        q.append((sr, sc))
        dirx = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = [[0] * m for _ in range(n)]
        
        while q:
            x, y = q.popleft()
            if image[x][y] != oldColor or visited[x][y]:
                continue
            
            visited[x][y] = 1
            image[x][y] = color
            for dx, dy in dirx:
                dx = x+dx
                dy = y+dy
                if 0 <= dx < n and 0 <= dy < m and image[dx][dy] == oldColor and not visited[dx][dy]:
                    q.append((dx, dy))
        
        return image