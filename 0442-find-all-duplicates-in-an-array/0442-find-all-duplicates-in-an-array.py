class Solution:
    def findDuplicates(self, nums):
        i = 0
        ans = []
        while i < len(nums):
            idx = nums[i]-1
            if nums[i] == -1 or nums[i] == i+1:
                i += 1

            elif nums[i] == nums[idx]:
                ans.append(nums[i])
                nums[i] = -1
                nums[idx] = -1
                
            elif nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
        
        return ans
