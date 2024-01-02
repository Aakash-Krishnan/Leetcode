class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            sub = []
            flag = False
            for j in range(len(nums)):
                if nums[j] == -1:
                    continue
                    
                elif not sub:
                    sub.append(nums[j])
                    nums[j] = -1
                    flag = True
                    
                elif sub[-1] != nums[j]:
                    sub.append(nums[j])
                    nums[j] = -1
                    flag = True
                    
            if not flag:
                return ans
                    
            ans.append(sub)
        return ans