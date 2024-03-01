class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = [[-1] * (sum(nums)+1) for _ in range(len(nums))]
        
        def dfs(i, Sum):
            if i >= len(nums):
                return Sum
            if cache[i][Sum] != -1:
                return cache[i][Sum]
            
            cache[i][Sum] = max(dfs(i+1, Sum) , dfs(i+2, Sum + nums[i]))
            return cache[i][Sum]
        
        return dfs(0, 0)
        