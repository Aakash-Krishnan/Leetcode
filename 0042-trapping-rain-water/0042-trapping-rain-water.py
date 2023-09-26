class Solution:
    def trap(self, height: List[int]) -> int:
        Pmax = [0]*len(height)
        Pmax[0] = height[0]
        
        Smax= [0]*len(height)
        Smax[-1] = height[-1]
        
        for i in range(1, len(height)):
            Pmax[i] = max(height[i], Pmax[i-1])
        
        for i in range(len(height)-2, -1, -1):
            Smax[i] = max(height[i], Smax[i+1])
        
        cnt = 0
        for i in range(1, len(height)-1):
            wl = min(Pmax[i-1], Smax[i+1])
            wt = max(0, wl - height[i])
            
            cnt += wt
        return cnt