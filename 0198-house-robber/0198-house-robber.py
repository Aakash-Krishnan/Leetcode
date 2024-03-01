class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = [-1 for _ in range(len(nums)+1)]
        
        def dfs(i, Sum=0):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i+1, Sum), nums[i] + dfs(i+2, Sum))
            return cache[i]
        
        return dfs(0)
        