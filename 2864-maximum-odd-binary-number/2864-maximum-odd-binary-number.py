class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        pos = len(s) - 1
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
        
        ones -= 1
        res = ""
        while pos:
            if ones:
                res = '1' + res
                ones -= 1
            else:
                res += '0'
            pos -= 1
        
        return res + "1"
            