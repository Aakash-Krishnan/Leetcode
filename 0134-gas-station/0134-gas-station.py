class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        carry = 0
        res = 0
        for i in range(len(gas)):
            carry += gas[i] - cost[i]
            if carry < 0:
                carry = 0
                res = i + 1
        return res