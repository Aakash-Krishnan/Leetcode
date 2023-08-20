class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                Sum = 0
                l = 0
                for m in range(i, j + 1):
                    Sum += nums[m]
                    l += 1
                if l % 2 != 0:
                    ans += Sum
        return ans