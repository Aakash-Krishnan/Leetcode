class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        timeMap = {}
        
        for src, dst, t in meetings:
            if t not in timeMap:
                timeMap[t] = defaultdict(list)
            timeMap[t][src].append(dst)
            timeMap[t][dst].append(src)
        
        def dfs(src, adj):
            if src in visit:
                return 
            secrets.add(src)
            visit.add(src)
            for nei in adj[src]:
                dfs(nei, adj)
        
        for time in sorted(timeMap.keys()):
            visit = set()
            for src in timeMap[time]:
                if src in secrets:
                    dfs(src, timeMap[time])
        
        return list(secrets)