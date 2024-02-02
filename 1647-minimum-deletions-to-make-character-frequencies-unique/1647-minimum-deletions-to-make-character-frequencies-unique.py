class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        cache = set()
        for char, cnt in count.items():
            if cnt in cache:
                while cnt and cnt in cache:
                    cnt -= 1
                    res += 1
            cache.add(cnt)
        return res