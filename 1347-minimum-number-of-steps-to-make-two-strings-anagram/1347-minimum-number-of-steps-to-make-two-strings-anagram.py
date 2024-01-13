class Solution:
    def minSteps(self, s: str, t: str) -> int:
        Scache = Counter(s)
        Tcache = Counter(t)
        tlen = len(t)
        for i in Tcache:
            if Scache[i]:
                if Scache[i] > Tcache[i]:
                    tlen -= Tcache[i]
                else:
                    tlen -= Scache[i]
        return tlen