class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        l = len(a) -1 
        r = len(b) -1 
        
        ans = ''
        
        while carry or l >= 0 or r >= 0:
            Sum = 0
            if l >= 0:
                Sum += int(a[l])
                l -= 1
            if r>= 0:
                Sum += int(b[r])
                r -= 1
            Sum += carry
            
            bit = Sum%2
            ans += str(bit)
            carry = Sum // 2
        
        return ans[::-1]