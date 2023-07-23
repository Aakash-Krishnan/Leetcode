class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, prod = 0, 1
        while n > 0:
            A = n % 10
            prod *= A
            sum += A
            n = n//10
        return prod - sum
        