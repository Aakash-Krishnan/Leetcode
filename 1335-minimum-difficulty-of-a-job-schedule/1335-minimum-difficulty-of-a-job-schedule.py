class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        if len(job) < d:
            return -1
        if len(job) == d:
            return sum(job)
        
        cache = {}
        def dfs(idx, d, currMax):
            if idx == len(job):
                return 0 if d == 0 else float('inf')
            if d == 0:
                return float('inf')
            
            if (idx, d, currMax) in cache:
                return cache[(idx, d, currMax)]
            
            currMax = max(currMax, job[idx])
            res = min(
                     dfs(idx + 1, d, currMax),
                     currMax + dfs(idx + 1, d - 1, -1)
                    )
            
            cache[(idx, d, currMax)] = res
            
            return res
        
        return dfs(0, d, -1)