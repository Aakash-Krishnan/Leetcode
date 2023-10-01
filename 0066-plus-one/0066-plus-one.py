class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                digits[i] += 1
            else:
                digits[i] += carry
            
            carry = digits[i] // 10
            digits[i] %= 10
        
        if carry:
            digits.insert(0, carry)
            return digits
        
        for i in range(len(digits)):
            if digits[i] != 0:
                return digits[i:]