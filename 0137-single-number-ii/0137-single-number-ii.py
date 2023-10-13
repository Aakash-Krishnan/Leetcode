class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for j in range(32):
            cnt = 0
            
            for i in range(len(nums)):
                if nums[i] < 0:
                    nums[i] = nums[i] & (2**32-1)
                cnt += nums[i] & (1<<j)
            
            if (cnt%3):
                ans |= (1<<j)
        if ans >= 2**31:
            ans -= 2**32
        return ans