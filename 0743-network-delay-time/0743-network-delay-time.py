class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for (u,v,w) in times:
            graph[u].append((w, v))
        inf = float("inf")
        delay = [inf] * (n+1)
        delay[0] = 0
        delay[k] = 0
        minHq = []
        heappush(minHq, (0, k))
        
        while minHq:
            time, node = heappop(minHq)
            
            for t, n in graph[node]:
                if delay[n] > t + time:
                    delay[n] = t + time
                    heappush(minHq, (time + t, n))
        
        for i in delay:
            if i == inf:
                return -1
        
        return max(delay)