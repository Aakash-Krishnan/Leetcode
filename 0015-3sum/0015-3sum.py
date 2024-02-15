class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i and a == nums[i-1]:
                continue
            
            L, R = i+1, len(nums)-1
            while L < R:
                val = a + nums[L] + nums[R]
                if val > 0:
                    R -= 1
                elif val < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
            
        return res