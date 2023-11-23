class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(sub):
            diff = 0
            for j in range(1, len(sub)):
                if j == 1:
                    diff = sub[j] - sub[j-1]
                elif sub[j] - sub[j-1] != diff:
                    return False    
            return True
        
        ans = []
        for i in range(len(l)):
            L = l[i]
            R = r[i] + 1
            sub = nums[L: R]
            sub.sort()
            ans.append(check(sub))
            
        return ans