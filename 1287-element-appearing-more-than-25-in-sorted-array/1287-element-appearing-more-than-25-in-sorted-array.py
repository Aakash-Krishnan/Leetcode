class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans = [0,0]
        cnt = 0
        curr = arr[0]
        
        for i in arr:
            if i == curr:
                cnt += 1
            else:
                curr = i
                cnt = 1
            
            if cnt > ans[0]:
                ans[0] = cnt
                ans[1] = curr
        
        return ans[1]