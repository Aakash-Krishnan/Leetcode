class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = [-1] * len(arr)
        
        def dfs(i):
            if i >= len(arr):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            currMax, res = 0, 0
            for j in range(i, min(len(arr), i+k)):
                currMax = max(currMax, arr[j])
                windowSize = j - i + 1
                res = max(res, dfs(j+1) + currMax * windowSize)
            cache[i] = res
            
            return cache[i]
        
        return dfs(0)