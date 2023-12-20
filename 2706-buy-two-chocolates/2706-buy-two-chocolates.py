class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        first = second = float("inf")
        
        for price in prices:
            if price < first:
                first, second = price, first
            elif price < second:
                second = price
        
        leftMoney = money - (first + second)
        return leftMoney if leftMoney >= 0 else money