class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        curr = 1
        res = [-1, -1]
        i = 0
        while i < N:
            if nums[i] == curr:
                i += 1
                if i < N and nums[i] == curr:
                    res[0] = nums[i]
                    i += 1
                curr += 1
            else:
                res[1] = curr
                curr += 1
        if res[1] == -1:
            res[1] = curr
            
        return res