class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        leftMoney = money
        cnt = 0
        prices.sort()
        print(prices)
        
        for i in prices:
            if i < money:
                cnt += 1
                leftMoney -= i
                
            if leftMoney < 0:
                return money
            
            if cnt == 2:
                return leftMoney
        
        return money