class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        degree = [0] * n
        
        for cour, prevCour in prerequisites:
            graph[prevCour].append(cour)
            degree[cour] += 1
        
        q = deque()
        res = []
        for i in range(n):
            if not degree[i]:
                q.append(i)
                res.append(i)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                degree[nei] -= 1
                if not degree[nei]:
                    q.append(nei)
                    res.append(nei)
        
        return res if len(res) == n else []