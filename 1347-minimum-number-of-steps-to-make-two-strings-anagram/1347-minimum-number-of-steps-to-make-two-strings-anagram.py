class Solution:
    def minSteps(self, s: str, t: str) -> int:
        Scache = Counter(s)
        Tcache = Counter(t)
        tlen = len(t)
        for i in Tcache:
            if Scache[i]:
                val = Scache[i]
                if val > Tcache[i]:
                    tlen -= Tcache[i]
                    Tcache[i] = 0
                else:
                    Tcache[i] -= val
                    tlen -= val
        return tlen