class Solution:
    def romanToInt(self, s: str) -> int:
        fmap = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        total = 0
        for i in range(len(s)-1):
            if fmap[s[i]] < fmap[s[i+1]]:
                total -= fmap[s[i]]
            else:
                total += fmap[s[i]]
        total += fmap[s[-1]]
        return total
                    
                