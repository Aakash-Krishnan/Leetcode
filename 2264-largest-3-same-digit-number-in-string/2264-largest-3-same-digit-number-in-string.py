class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        ans = ""
        L, R = 0, 2
        while R < len(nums):
            if nums[L] == nums[L+1] == nums[R]:
                if ans == "" or int(nums[L]) > int(ans[0]):
                    ans = nums[L:R+1]
            L += 1
            R += 1
        return ans