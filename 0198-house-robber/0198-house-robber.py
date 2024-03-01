class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        
        def dfs(i, Sum):
            if i >= len(nums):
                return Sum
            if (i, Sum) in cache:
                return cache[(i, Sum)]
            
            cache[(i, Sum)] = max(dfs(i+1, Sum) , dfs(i+2, Sum + nums[i]))
            return cache[(i, Sum)]
        
        return dfs(0, 0)
        