class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        m = len(l)
        for i in range(m):
            sub = []
            L = l[i]
            R = r[i] + 1
            for j in range(L, R):
                sub.append(nums[j])
            sub.sort()
            diff = 0
            flag= False
            for j in range(1, len(sub)):
                if j == 1:
                    diff = sub[j] - sub[j-1]
                elif sub[j] - sub[j-1] != diff:
                    flag = True
                    ans.append(False)
                    break
            if not flag:
                ans.append(True)
        
        return ans