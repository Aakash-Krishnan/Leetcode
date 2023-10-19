class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10**9
        Sum = 0
        
        for i in nums:
            Sum += i
            if Sum > ans:
                ans = Sum
            
            if Sum < 0:
                Sum = 0
        return ans