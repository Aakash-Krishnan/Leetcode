class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        val = strs[0]
        
        for i in range(1, len(strs)):
            l = 0
            while l < len(val) and l < len(strs[i]):
                if strs[i][l] != val[l]:
                    break
                l += 1
            val = val[:l]
        return val
        