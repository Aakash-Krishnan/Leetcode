class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        cache = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cache[i][diff] += 1 + cache[j][diff]
                res += cache[j][diff]
        
        return res