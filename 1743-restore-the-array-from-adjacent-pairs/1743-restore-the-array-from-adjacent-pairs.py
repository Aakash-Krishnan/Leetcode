class Solution:
    def restoreArray(self, A: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x, y in A:
            adj[x].append(y)
            adj[y].append(x)
        
        res = []
        for num, nei in adj.items():
            if len(nei) == 1:
                res = [num, nei[0]]
                break
        
        while len(res) < len(A) + 1:
            prev, curr = res[-2], res[-1]
            
            for nei in adj[curr]:
                if nei != prev:
                    prev = curr
                    res.append(nei)
                    break
        
        return res