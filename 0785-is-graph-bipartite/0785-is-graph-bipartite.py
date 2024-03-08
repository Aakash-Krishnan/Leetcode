class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)
        
        def bfs(node):
            if odd[node]:
                return True
            
            q = deque([node])
            odd[node] = -1
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if odd[nei] == odd[node]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[node]
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True