class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        graph = defaultdict(list)
        
        for sec, first in prerequisites:
            graph[first].append(sec)
            degree[sec] += 1
        
        q = deque()
        for node, ideg in enumerate(degree):
            if not ideg:
                q.append(node)
        
        nodes = set()
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                nodes.add(node)
                for nei in graph[node]:
                    degree[nei] -= 1
                    if not degree[nei]:
                        q.append(nei)
                
        return len(nodes) == numCourses