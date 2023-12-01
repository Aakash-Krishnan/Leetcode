class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Sum1 = ""
        Sum2 = ""
        for i in word1:
            Sum1+= i
        for i in word2:
            Sum2+= i
        sorted(Sum1)
        sorted(Sum2)
        return Sum1 == Sum2
        