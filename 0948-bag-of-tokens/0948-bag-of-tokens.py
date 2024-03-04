class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        l, r = 0, len(tokens) - 1
        cnt = 0
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                cnt += 1
                l += 1
            elif cnt:
                power += tokens[r]
                cnt -= 1
                r -= 1
            else:
                break
            res = max(res, cnt)
        
        return res