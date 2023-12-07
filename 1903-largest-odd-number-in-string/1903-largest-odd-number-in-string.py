class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = -1
        for i in range(len(num)):
            if int(num[i]) & 1:
                idx = i
        
        return "" if idx == -1 else num[: idx+1]