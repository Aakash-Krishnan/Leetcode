class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [0] * (len(nums))
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            if cache[i]:
                return cache[i]
            
            res = len(nums)
            for j in range(1, nums[i]+1):
                res = min(res, 1 + dfs(i+j))
            
            cache[i] = res
            return res
        
        dfs(0)
        return cache[0]