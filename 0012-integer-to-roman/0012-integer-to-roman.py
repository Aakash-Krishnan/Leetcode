class Solution:
    def intToRoman(self, num: int) -> str:
        fmap = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        ans = ""
        while num != 0:
            id = 0
            for i in fmap:
                if num >= i:
                    id = i
                else:
                    break
            while True:
                ans += fmap[id]
                num -= id
                if num < id:
                    break
        return ans