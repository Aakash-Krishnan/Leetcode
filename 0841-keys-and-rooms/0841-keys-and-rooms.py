class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        root = [i for i in range(n)]
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        
        def dfs(node):
            for nei in rooms[node]:
                x = find(node)
                y = find(nei)
                if x != y:
                    root[y] = root[x]
                    dfs(nei)
        
        
        dfs(0)
        
        for i in range(1, len(root)):
            if root[i] != root[i-1]:
                return False
        
        return True