class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        val = strs[0]
        for i in range(len(val)):
            for str in strs[1:]:
                if (i == len(str)) or str[i] != val[i]:
                    return val[0:i]
                
            
        return val
                
                