class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}
        
        def helper(idx, k, prev, prevCount):
            if (idx, k, prev, prevCount) in cache:
                return cache[(idx, k, prev, prevCount)]
            
            if k < 0:
                return float("inf")
            
            if idx == len(s):
                return 0
            
            if s[idx] == prev:
                inc = 1 if prevCount in [1, 9, 99] else 0
                res = inc + helper(idx + 1, k, prev, prevCount + 1)
            
            else:
                res = min(helper(idx + 1, k - 1, prev, prevCount),
                        1 + helper(idx + 1, k, s[idx], 1))
            
            cache[(idx, k, prev, prevCount)] = res
            return res
        
        return helper(0, k, "", 0)