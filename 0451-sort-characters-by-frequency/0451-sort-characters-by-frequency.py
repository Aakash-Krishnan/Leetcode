class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        hq = []
        for char, freq in count.items():
            heappush(hq, (-freq, char))
        res = ""
        while hq:
            val, char = heappop(hq)
            res += char * (-val)
        return res