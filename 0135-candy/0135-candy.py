class Solution:
    def candy(self, ratings: List[int]) -> int:
        Sum = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                Sum[i] = Sum[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                Sum[i] = max(Sum[i], Sum[i+1] + 1)
        
        return sum(Sum)