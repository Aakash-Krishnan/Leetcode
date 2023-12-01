class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Sum1 = "".join(word1)
        Sum2 = "".join(word2)
        # n,m = len(word1), len(word2)
        # for i in range(max(n, m)):
        #     if i < n:
        #         Sum1 += word1[i]
        #     if i < m:
        #         Sum2+= word2[i]
        return Sum1 == Sum2