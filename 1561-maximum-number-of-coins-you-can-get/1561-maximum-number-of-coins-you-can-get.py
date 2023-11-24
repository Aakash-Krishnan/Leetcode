class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i, j = 1, len(piles)-1
        Sum = 0
        while i < j:
            Sum += piles[i]
            i += 2
            j -= 1
        return Sum