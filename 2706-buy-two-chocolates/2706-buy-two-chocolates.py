class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        leftMoney = money
        cnt = 0
        
        for i in sorted(prices):
            if i < money:
                cnt += 1
                leftMoney -= i
                
            if leftMoney < 0:
                return money
            
            if cnt == 2:
                return leftMoney
        
        return money