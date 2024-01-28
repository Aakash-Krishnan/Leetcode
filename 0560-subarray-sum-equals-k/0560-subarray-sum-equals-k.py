class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        cache[0] = 1
        pSum = 0
        res = 0
        for i in range(len(nums)):
            pSum += nums[i]
            if pSum - k in cache:
                res += cache[pSum - k]      
            cache[pSum] += 1
        
        return res
                