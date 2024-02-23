class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe = {}
        
        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    safe[nei] = False
                    return safe[nei]
                
            safe[node] = True
            return safe[node]
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
            
        return res