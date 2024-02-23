class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for (u, v, w) in flights:
            graph[u].append((w, v))
            
        q = deque()        
        q.append((0, -1, src))
        inf = float("inf")
        dist = [inf] * (n)
        dist[src] = 0

        while q:
            cost, steps, node = q.popleft()
            if steps >= k:
                continue
            
            for c, city in graph[node]:
                if dist[city] > cost + c:
                    dist[city] = cost + c
                    q.append((cost + c, steps + 1, city))
        
        return dist[dst] if dist[dst] != inf else -1