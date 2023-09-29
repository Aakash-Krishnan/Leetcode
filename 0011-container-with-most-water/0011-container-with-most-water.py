class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans= 0
        lMax = height[0]
        rMax = height[-1]
        l = 0
        r = len(height)-1
        
        while l < r:
            if lMax < rMax:
                ans = max(ans, height[l]*(r-l))
                l += 1
                lMax = max(lMax, height[l])
            else:
                ans = max(ans, height[r]*(r-l))
                r -= 1
                rMax = max(rMax, height[r])
        return ans
        