class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHq = [(-cnt, val) for val, cnt in counter.items()]
        heapify(maxHq)
        prev = None
        res = ""
        while prev or maxHq:
            if prev and not maxHq:
                return ""
            cnt, char = heappop(maxHq)
            cnt += 1
            res += char
            if prev:
                heappush(maxHq, prev)
                prev = None
            if cnt:
                prev = (cnt, char)
            
        return res